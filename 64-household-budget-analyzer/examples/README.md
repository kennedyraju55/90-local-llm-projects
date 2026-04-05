# Examples for Household Budget Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from YAML file.
- **`get_config()`** — Return cached configuration, loading on first call.
- **`setup_logging()`** — Configure logging for the application.
- **`load_expenses()`** — Load expenses from a CSV file.
- **`filter_by_month()`** — Filter expenses by month string like 'March 2024'.
- **`SavingsGoal`** — Track progress toward a savings goal.

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
