# Examples for Survey Response Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`get_llm_client()`** — Get LLM client with proper path setup.
- **`load_survey_data()`** — Load survey responses from a CSV file.
- **`identify_text_columns()`** — Identify columns likely containing free-text responses.
- **`identify_demographic_columns()`** — Identify columns that are likely demographic/categorical.

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
