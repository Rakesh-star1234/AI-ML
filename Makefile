PYTHON ?= python
VENV := .venv

ifeq ($(OS),Windows_NT)
    PYTHON_VENV := $(VENV)\Scripts\python.exe
else
    PYTHON_VENV := $(VENV)/bin/python
endif

.PHONY: install test lint run clean

install:
	$(PYTHON) -m venv $(VENV)
	$(PYTHON_VENV) -m pip install --upgrade pip
	$(PYTHON_VENV) -m pip install -r requirements.txt
	$(PYTHON_VENV) -m pip install -e .

test:
	$(PYTHON_VENV) -m pytest -q

lint:
	$(PYTHON_VENV) -m ruff check src tests

run:
	$(PYTHON_VENV) -m basic_project

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
