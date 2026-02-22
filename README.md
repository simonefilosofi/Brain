# 🧠 Brain 
A minimal CLI tool for taking and searching personal notes, powered by SQLite.

Because my actual brain is busy forgetting things.

## Install

```bash
git clone https://github.com/simonefilosofi/brain.git
cd brain
pip install -e .
```

After installing, make sure pip's script directory is on your `$PATH`.
If `brain` is not found after install, your `$PATH` is lying to you. Run this to find the truth:

```bash
python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))"
```

Add the printed path to your shell config (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export PATH="/path/from/above:$PATH"
```

Then reload it (yes, you have to do this, no, it won't work without it):

```bash
source ~/.zshrc   # or ~/.bashrc
```

## Usage

```bash
# Had a thought? Quick, before it's gone
brain add "Read the pragmatic programmer"

# Stare at everything you said you'd do
brain list

# Pretend you remember what you wrote
brain find "pragmatic"

# Feel accomplished without actually doing anything
brain check 3

# Just kidding, you're not done yet
brain uncheck 3

# Commit to the bit
brain delete 3
```

## Notes storage

Notes are stored in `~/.brain/brain.db` (SQLite). The directory is created automatically on first use, unlike your motivation, which you have to find yourself 👀.

## Requirements

- Python 3.10+ (if you're on 3.9, this is a sign to update your life)
- [typer](https://typer.tiangolo.com/) – CLI framework
- [rich](https://rich.readthedocs.io/) – makes the terminal pretty, which is more than can be said for most things

Dependencies are installed automatically by `pip install -e .` — one of the few things in life that just works.
