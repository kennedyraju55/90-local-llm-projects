# Examples for Stock Report Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`get_llm_client()`** — Get LLM client with proper path setup.
- **`load_stock_data()`** — Load stock data from a CSV file.
- **`compute_metrics()`** — Compute basic technical analysis metrics from stock data.
- **`compute_technical_indicators()`** — Compute advanced technical indicators.

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
