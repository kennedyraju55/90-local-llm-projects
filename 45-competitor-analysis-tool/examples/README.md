# Examples for Competitor Analysis Tool

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`get_llm_client()`** — Get LLM client with proper path setup.
- **`generate_swot()`** — Generate SWOT analysis for the company vs competitors.
- **`generate_feature_matrix()`** — Generate a feature comparison matrix.
- **`generate_pricing_comparison()`** — Generate pricing comparison analysis.

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
