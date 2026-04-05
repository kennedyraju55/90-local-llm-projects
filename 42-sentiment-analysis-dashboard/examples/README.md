# Examples for Sentiment Analysis Dashboard

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`get_llm_client()`** — Get LLM client with proper path setup.
- **`read_text_file()`** — Read a text file and return non-empty lines.
- **`read_batch_files()`** — Read multiple text files for batch processing.
- **`analyze_sentiment()`** — Analyze sentiment of a single text entry.

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
