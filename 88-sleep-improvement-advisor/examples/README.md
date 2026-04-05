# Examples for Sleep Improvement Advisor

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`parse_sleep_log()`** — Parse a sleep log CSV file.
- **`compute_sleep_stats()`** — Compute summary statistics from sleep log entries.
- **`calculate_sleep_score()`** — Calculate a sleep score from 0-100 based on sleep statistics.
- **`get_environment_checklist()`** — Return the sleep environment optimization checklist.
- **`build_bedtime_routine()`** — Build a personalized bedtime routine based on desired wake time.

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
