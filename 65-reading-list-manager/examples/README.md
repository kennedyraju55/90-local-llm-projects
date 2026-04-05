# Examples for Reading List Manager

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from config.yaml.
- **`load_books()`** — Load reading list from JSON file.
- **`save_books()`** — Save reading list to JSON file.
- **`add_book()`** — Add a book to the reading list.
- **`update_progress()`** — Track reading progress – pages read and percent complete.

## Prerequisites

- Python 3.10+
- Ollama running with Gemma 4 model
- Project dependencies installed (`pip install -e .`)

## Running

From the project root directory:

```bash
# Install the project in development mode
pip install -e .

# Run the demo
python examples/demo.py
```
