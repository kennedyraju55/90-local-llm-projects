# Examples for Symptom Checker Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml or use defaults.
- **`assess_urgency()`** — Assess urgency level based on symptom keywords.
- **`get_body_regions()`** — Identify which body regions are affected by the described symptoms.
- **`display_disclaimer()`** — Display the medical disclaimer using rich formatting.
- **`check_symptoms()`** — Analyse symptoms using the LLM and return the response text.
- **`MedicalHistoryTracker`** — Track symptom history across a session.

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
