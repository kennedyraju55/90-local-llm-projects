# Examples for Smart Calendar Assistant

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`get_config()`** — Return the cached application config, loading it on first access.
- **`load_schedule()`** — Load schedule events from a JSON file.
- **`display_schedule()`** — Return a human-readable text representation of the schedule.
- **`optimize_schedule()`** — Use the LLM to suggest an optimized ordering / grouping of events.

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
