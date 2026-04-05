# Examples for Habit Tracker Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML, falling back to defaults.
- **`load_habits()`** — Load habits data from JSON file.
- **`save_habits()`** — Save habits data to JSON file.
- **`log_habit()`** — Log a habit completion for today.
- **`add_habit()`** — Add a new habit definition.

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
