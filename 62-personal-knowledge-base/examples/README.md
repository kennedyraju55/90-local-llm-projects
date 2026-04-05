# Examples for Personal Knowledge Base

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml, falling back to sensible defaults.
- **`load_kb()`** — Load the knowledge base from JSON file.
- **`save_kb()`** — Save the knowledge base to JSON file.
- **`add_note()`** — Add a note to the knowledge base.
- **`delete_note()`** — Delete a note by ID. Returns True if deleted, False if not found.

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
