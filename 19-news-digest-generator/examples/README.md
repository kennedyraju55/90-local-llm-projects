# Examples for News Digest Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`read_news_files()`** — Read all .txt files from the sources directory.
- **`categorize_articles()`** — Send articles to the LLM for topic categorization.
- **`generate_digest()`** — Generate an overall news digest from the categorized articles.
- **`analyze_sentiment()`** — Analyze sentiment across articles.
- **`save_output()`** — Save the digest output to a file.

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
