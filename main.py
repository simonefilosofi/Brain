import sqlite3
from datetime import datetime
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table
from rich import box

app = typer.Typer(help="Brain – your personal note-taking CLI.")
console = Console()

DB_PATH = Path.home() / ".brain" / "brain.db"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            content    TEXT    NOT NULL,
            created_at TEXT    NOT NULL,
            done       INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    # Migration: add 'done' column if it doesn't exist yet (for existing databases)
    columns = [row[1] for row in conn.execute("PRAGMA table_info(notes)").fetchall()]
    if "done" not in columns:
        conn.execute("ALTER TABLE notes ADD COLUMN done INTEGER NOT NULL DEFAULT 0")
    conn.commit()
    return conn


def _render_table(rows: list[tuple], title: str) -> None:
    if not rows:
        console.print("[dim]No notes found.[/dim]")
        return

    table = Table(
        title=title,
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold cyan",
    )
    table.add_column("ID", style="dim", justify="right", no_wrap=True)
    table.add_column("", justify="center", no_wrap=True)
    table.add_column("Note", style="white")
    table.add_column("Created at", style="green", no_wrap=True)

    for row_id, content, created_at, done in rows:
        tick = "[bold green]✓[/bold green]" if done else "[dim]○[/dim]"
        note_style = "dim strike" if done else "white"
        table.add_row(str(row_id), tick, f"[{note_style}]{content}[/{note_style}]", created_at)

    console.print(table)


@app.command()
def add(note: str = typer.Argument(..., help="The note text to save.")):
    """Save a new note with the current timestamp."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO notes (content, created_at, done) VALUES (?, ?, 0)", (note, now)
        )
        note_id = cur.lastrowid
    console.print(f"[bold green]✓[/bold green] Note [cyan]#{note_id}[/cyan] saved.")


@app.command("list")
def list_notes():
    """Show all notes, most recent first."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, content, created_at, done FROM notes ORDER BY done ASC, id DESC"
        ).fetchall()
    _render_table(rows, "All Notes")


@app.command()
def find(keyword: str = typer.Argument(..., help="Keyword to search for (case-insensitive).")):
    """Search notes by keyword."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, content, created_at, done FROM notes WHERE content LIKE ? ORDER BY done ASC, id DESC",
            (f"%{keyword}%",),
        ).fetchall()
    _render_table(rows, f'Search results for "{keyword}"')

@app.command()
def edit(note_id: int = typer.Argument(..., help="ID of the note to edit."),
    new_content: str = typer.Argument(..., help="New content for the note."),
):
    """Edit the content of an existing note."""
    with get_connection() as conn:
        row = conn.execute("SELECT id, content FROM notes WHERE id = ?", (note_id,)).fetchone()
        if not row:
            console.print(f"[red]✗[/red] No note found with ID [cyan]#{note_id}[/cyan].")
            raise typer.Exit(code=1)
        conn.execute("UPDATE notes SET content = ? WHERE id = ?", (new_content, note_id))
    console.print(f"[bold green]✓[/bold green] Note [cyan]#{note_id}[/cyan] updated.")
    console.print(f"  [dim]Before:[/dim] {row[1]}")
    console.print(f"  [dim]After: [/dim] {new_content}")


@app.command()
def check(note_id: int = typer.Argument(..., help="ID of the note to mark as done.")):
    """Mark a note as done."""
    with get_connection() as conn:
        row = conn.execute("SELECT id, content, done FROM notes WHERE id = ?", (note_id,)).fetchone()
        if not row:
            console.print(f"[red]✗[/red] No note found with ID [cyan]#{note_id}[/cyan].")
            raise typer.Exit(code=1)
        if row[2]:
            console.print(f"[dim]Note [cyan]#{note_id}[/cyan] is already marked as done.[/dim]")
            raise typer.Exit()
        conn.execute("UPDATE notes SET done = 1 WHERE id = ?", (note_id,))
    console.print(f"[bold green]✓[/bold green] Note [cyan]#{note_id}[/cyan] marked as done: [dim strike]{row[1]}[/dim strike]")


@app.command()
def uncheck(note_id: int = typer.Argument(..., help="ID of the note to mark as not done.")):
    """Mark a note as not done."""
    with get_connection() as conn:
        row = conn.execute("SELECT id, content, done FROM notes WHERE id = ?", (note_id,)).fetchone()
        if not row:
            console.print(f"[red]✗[/red] No note found with ID [cyan]#{note_id}[/cyan].")
            raise typer.Exit(code=1)
        if not row[2]:
            console.print(f"[dim]Note [cyan]#{note_id}[/cyan] is already marked as not done.[/dim]")
            raise typer.Exit()
        conn.execute("UPDATE notes SET done = 0 WHERE id = ?", (note_id,))
    console.print(f"[bold yellow]○[/bold yellow] Note [cyan]#{note_id}[/cyan] marked as not done.")


@app.command()
def delete(note_id: int = typer.Argument(..., help="ID of the note to delete.")):
    """Delete a note by its ID."""
    with get_connection() as conn:
        row = conn.execute("SELECT id, content FROM notes WHERE id = ?", (note_id,)).fetchone()
        if not row:
            console.print(f"[red]✗[/red] No note found with ID [cyan]#{note_id}[/cyan].")
            raise typer.Exit(code=1)
        console.print(f"[dim]Deleting:[/dim] {row[1]}")
        confirmed = typer.confirm("Are you sure?")
        if not confirmed:
            console.print("[dim]Aborted.[/dim]")
            raise typer.Exit()
        conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    console.print(f"[bold red]✓[/bold red] Note [cyan]#{note_id}[/cyan] deleted.")


@app.command()
def brain():
    """Display the brain image."""
    import subprocess
    import os

    script_path = os.path.join(os.path.dirname(__file__), "brain_image.py")
    subprocess.run(["python3", script_path])

if __name__ == "__main__":
    app()