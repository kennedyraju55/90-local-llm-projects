# Examples for Time Management Coach

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`load_timelog()`** — Load time log entries from a CSV file.
- **`save_time_entry()`** — Append a single time entry to the CSV log, creating the file if needed.
- **`compute_time_breakdown()`** — Compute total hours per category.
- **`compute_daily_totals()`** — Compute total hours per day.

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
