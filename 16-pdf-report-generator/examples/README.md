# Examples for Pdf Report Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`read_csv_data()`** — Read CSV file and return headers and rows.
- **`summarize_data()`** — Build a statistical summary of the CSV data for LLM context.
- **`generate_report()`** — Use the LLM to generate a structured markdown report.
- **`save_report()`** — Save the generated report to a file with metadata header.

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
