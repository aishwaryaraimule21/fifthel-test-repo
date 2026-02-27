# Greeter CLI

A small command-line app that greets a user by name in different languages.  
This package is intended for **code review demos**: the structure is simple and easy to follow.

## Package layout

| File        | Purpose |
|------------|---------|
| `config.py` | Default language and greeting templates (en, es, fr). |
| `greeter.py` | Core logic: `greet(name, lang)` returns a greeting string. |
| `main.py`   | CLI: parses `name` and `--lang`, then prints the greeting. |

## Usage

From the **repository root** (so that `greeter_cli` is on the path):

```bash
# Using the convenience script (use python3 if python is not available)
python run_greeter.py Alice
python run_greeter.py Bob --lang es

# Or run the package module
python -m greeter_cli.main Alice -l fr
```

## Adding a language

Edit `config.py` and add an entry to the `GREETINGS` dict, e.g.:

```python
"de": "Hallo, {name}!",
```

Then use `--lang de` when running the CLI.
