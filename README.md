# AI-ML

This repository now includes a minimal Python project scaffold for learning and quick experiments.

## Project structure

- `src/basic_project/` contains the application package
- `tests/` contains pytest checks
- `Makefile` provides common developer commands

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make test
make run
```

On Windows PowerShell, use:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
make test
python -m basic_project
```

## Available commands

- `make install` — create the virtual environment and install dependencies
- `make test` — run the test suite
- `make lint` — run Ruff lint checks
- `make run` — execute the project entry point
- `make clean` — remove build and cache artifacts
