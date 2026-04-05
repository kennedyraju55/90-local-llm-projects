# Examples for Csv Data Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`get_llm_client()`** — Get LLM client with proper path setup.
- **`load_csv()`** — Load a CSV file into a pandas DataFrame.
- **`detect_column_types()`** — Auto-detect and categorize column types.
- **`generate_statistical_summary()`** — Generate comprehensive statistical summaries.

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
