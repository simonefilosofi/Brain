# Brain

A minimal CLI tool for taking and searching personal notes, powered by SQLite.

## Install

```bash
git clone https://github.com/simonefilosofi/brain.git
cd brain
pip install -e .
```

After installing, make sure pip's script directory is on your `$PATH`.
If `brain` is not found after install, run:

```bash
python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))"
```

Add the printed path to your shell config (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export PATH="/path/from/above:$PATH"
```

Then reload it:

```bash
source ~/.zshrc   # or ~/.bashrc
```

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

## Requirements

- Python 3.10+
- [typer](https://typer.tiangolo.com/) – CLI framework
- [rich](https://rich.readthedocs.io/) – terminal formatting

Dependencies are installed automatically by `pip install -e .`
