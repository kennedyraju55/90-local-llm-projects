# Examples for Standup Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`load_tasks()`** — Load tasks from a JSON file or return inline dict/list.
- **`get_git_log()`** — Get git log for the specified number of days, optionally filtered by author.
- **`get_git_branches()`** — Get list of git branches in the repository.
- **`categorize_tasks()`** — Categorize tasks into completed, in_progress, planned, and blocked.

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
