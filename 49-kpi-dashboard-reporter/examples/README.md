# Examples for Kpi Dashboard Reporter

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`load_kpi_data()`** — Load KPI data from a CSV file.
- **`safe_float()`** — Safely convert a value to float, stripping $, %, and commas.
- **`compute_kpi_trends()`** — Compute trends and changes for each KPI column.
- **`track_goals()`** — Compare KPI actuals vs target values.

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
