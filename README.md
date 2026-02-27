# Code Review Demo Repository

This repository contains a small Python project suitable for **code review demos**. The structure is simple and easy to understand so reviewers can focus on process and feedback style.

## What’s in this repo

- **`greeter_cli/`** – A minimal CLI that greets a user by name in different languages (English, Spanish, French). Good for reviewing modules, config, and a single entry point.
- **`hello_world.py`** – A standalone “Hello, World!” script (optional placeholder).
- **`run_greeter.py`** – Script to run the Greeter CLI from the repo root.

## Quick start

1. **Clone and enter the repo** (if needed):
   ```bash
   cd /path/to/fifthel-test-repo
   ```

2. **Run the Greeter CLI** (no install required; use the repo root as working directory):
   ```bash
   python run_greeter.py Alice
   python run_greeter.py Bob --lang es
   python run_greeter.py Carol -l fr
   ```
   Use `python3` instead of `python` if that’s what your system provides.

3. **Optional:** Use a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or: .venv\Scripts\activate on Windows
   # requirements.txt has no external deps; venv is for isolation
   ```

## Project structure

```
.
├── README.md                 # This file
├── requirements.txt         # Dependencies (none for this demo)
├── run_greeter.py           # Run the CLI from repo root
├── hello_world.py           # Simple placeholder script
└── greeter_cli/             # Main demo package
    ├── README.md            # Package-level docs
    ├── __init__.py
    ├── config.py            # Languages and greeting templates
    ├── greeter.py           # greet(name, lang) logic
    └── main.py              # argparse and CLI entry point
```

## Using this for code review

- **Scope:** One small app (`greeter_cli`) with config, logic, and CLI clearly separated.
- **READMEs:** Root and package READMEs describe purpose, layout, and how to run.
- **Simplicity:** No database or external APIs; easy to read and comment on in a short session.

You can walk through `config.py` → `greeter.py` → `main.py` and use this repo to practice review comments, style feedback, and small refactors.
