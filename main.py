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
            created_at TEXT    NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def _render_table(rows: list[tuple], title: str) -> None:
    if not rows:
        console.print(f"[dim]No notes found.[/dim]")
        return

    table = Table(
        title=title,
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold cyan",
    )
    table.add_column("ID", style="dim", justify="right", no_wrap=True)
    table.add_column("Note", style="white")
    table.add_column("Created at", style="green", no_wrap=True)

    for row_id, content, created_at in rows:
        table.add_row(str(row_id), content, created_at)

    console.print(table)


@app.command()
def add(note: str = typer.Argument(..., help="The note text to save.")):
    """Save a new note with the current timestamp."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO notes (content, created_at) VALUES (?, ?)", (note, now)
        )
        note_id = cur.lastrowid
    console.print(f"[bold green]✓[/bold green] Note [cyan]#{note_id}[/cyan] saved.")


@app.command("list")
def list_notes():
    """Show all notes, most recent first."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, content, created_at FROM notes ORDER BY id DESC"
        ).fetchall()
    _render_table(rows, "All Notes")


@app.command()
def find(keyword: str = typer.Argument(..., help="Keyword to search for (case-insensitive).")):
    """Search notes by keyword."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, content, created_at FROM notes WHERE content LIKE ? ORDER BY id DESC",
            (f"%{keyword}%",),
        ).fetchall()
    _render_table(rows, f'Search results for "{keyword}"')


if __name__ == "__main__":
    app()
