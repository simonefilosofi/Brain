# Brain

A minimal CLI tool for taking and searching personal notes, powered by SQLite.

## Install

```bash
# Clone / enter the project directory, then:
pip install -e .
```

This registers the `brain` command globally in your Python environment.

## Usage

```bash
# Add a note
brain add "Read the pragmatic programmer"

# List all notes (most recent first)
brain list

# Search notes by keyword (case-insensitive)
brain find "pragmatic"
```

## Notes storage

Notes are stored in `~/.brain/brain.db` (SQLite). The directory is created automatically on first use.

## Dependencies

- [typer](https://typer.tiangolo.com/) – CLI framework
- [rich](https://rich.readthedocs.io/) – terminal formatting
