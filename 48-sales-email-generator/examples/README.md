# Examples for Sales Email Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file.
- **`generate_email()`** — Generate a personalised sales email via the LLM.
- **`generate_variants()`** — Generate multiple email variants for A/B testing.
- **`research_prospect()`** — Use the LLM to generate a research profile for the prospect.
- **`generate_follow_up_sequence()`** — Generate a multi-email follow-up sequence.

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
