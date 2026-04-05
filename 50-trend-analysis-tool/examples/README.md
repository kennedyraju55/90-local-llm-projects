# Examples for Trend Analysis Tool

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`setup_logging()`** — Configure the logging subsystem from *config*.
- **`load_text_files()`** — Load text files from *directory*.
- **`extract_topics()`** — Extract topics and trends from *documents* via LLM.
- **`analyze_sentiment_trends()`** — Analyse sentiment patterns across *documents*.

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
