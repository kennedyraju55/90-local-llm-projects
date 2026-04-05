# Examples for Patient Intake Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml or use defaults.
- **`INTAKE_CATEGORIES`** — Standard intake form categories for medical history extraction.
- **`summarize_intake()`** — Summarize patient intake form text into a clinical summary.
- **`extract_medical_history()`** — Extract and categorize medical history from intake text.
- **`generate_pre_visit_summary()`** — Generate a pre-visit summary for the physician.
- **`identify_risk_factors()`** — Identify clinical risk factors from intake text.
- **`flag_missing_info()`** — Flag missing or incomplete information in the intake form.
- **`IntakeSession`** — Track intake summaries across a session.

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
