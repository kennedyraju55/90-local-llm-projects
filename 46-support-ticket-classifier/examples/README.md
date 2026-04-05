# Examples for Support Ticket Classifier

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file.
- **`load_tickets()`** — Load support tickets from a CSV file.
- **`find_text_column()`** — Identify the column most likely containing ticket descriptions.
- **`classify_ticket()`** — Classify a single support ticket via the LLM.
- **`classify_tickets_batch()`** — Classify a list of tickets. Returns parallel list of classification dicts.

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
