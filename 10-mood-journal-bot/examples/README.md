# Examples for Mood Journal Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_entries()`** — Load journal entries from the JSON file.
- **`save_entries()`** — Save journal entries to the JSON file.
- **`add_entry()`** — Create and save a new journal entry.
- **`get_recent_entries()`** — Get entries from the last N days.
- **`analyze_entries()`** — Analyze mood patterns in journal entries using LLM.

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
