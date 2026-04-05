# Examples for Sql Query Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`read_schema()`** — Read a SQL schema file.
- **`parse_schema_text()`** — Extract table info from schema text.
- **`get_table_names()`** — Extract table names from schema text.
- **`visualize_schema()`** — Generate a text-based schema visualization.

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
