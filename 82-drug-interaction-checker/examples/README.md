# Examples for Drug Interaction Checker

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml, falling back to defaults.
- **`parse_medications()`** — Parse a comma-separated medication string into a cleaned list.
- **`check_interactions()`** — Send medication list to the LLM for interaction analysis.
- **`get_food_interactions()`** — Look up known food interactions for a medication.
- **`get_dosage_notes()`** — Look up typical dosage notes for a medication.

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
