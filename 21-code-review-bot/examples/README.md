# Examples for Code Review Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`review_single_file()`** — Review a single code file and return structured results.
- **`review_multiple_files()`** — Review multiple files and return aggregated results.
- **`generate_autofix()`** — Generate auto-fix suggestions based on review results.
- **`export_report()`** — Export review results to a file.

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
