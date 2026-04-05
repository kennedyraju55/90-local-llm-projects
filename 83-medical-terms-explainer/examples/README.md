# Examples for Medical Terms Explainer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml.
- **`explain_term()`** — Explain a single medical term using the LLM.
- **`get_pronunciation()`** — Look up the phonetic pronunciation of a medical term.
- **`get_visual_aid()`** — Look up a visual-aid reference for a medical topic.
- **`get_related_conditions()`** — Return a list of conditions related to the given term.

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
