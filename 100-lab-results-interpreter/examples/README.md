# Examples for Lab Results Interpreter

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`display_disclaimer()`** — Display the medical disclaimer.
- **`load_config()`** — Load configuration from config.yaml or defaults.
- **`get_reference_range()`** — Look up reference ranges for a specific test.
- **`LAB_PANELS`** — List all supported lab panel types.
- **`REFERENCE_RANGES`** — View reference ranges for common tests.
- **`LabSession`** — Track lab result interpretations across a session.

## LLM-Powered Functions (require Ollama)

- **`interpret_results()`** — Full AI interpretation of lab results.
- **`identify_abnormalities()`** — Detect and explain abnormal values.
- **`suggest_followup_tests()`** — Get follow-up test recommendations.
- **`explain_lab_value()`** — Detailed explanation of a single lab value.

## Prerequisites

- Python 3.10+
- Ollama running with Gemma 4 model (`ollama pull gemma4`)
- Project dependencies installed (`pip install -e .`)

## Running

From the project root directory:

```bash
# Install the project in development mode
pip install -e .

# Run the demo
python examples/demo.py
```
