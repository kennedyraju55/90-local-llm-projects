# Examples for Ehr Deidentifier

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`regex_preprocess()`** — Apply regex-based PII detection before LLM processing.
- **`configurable_regex_preprocess()`** — Apply configurable regex-based PII detection.
- **`deidentify_text()`** — De-identify text using regex pre-processing followed by LLM analysis.
- **`read_file()`** — Read text content from a file.
- **`AuditLog`** — Audit log for de-identification operations.
- **`ValidationReport`** — Generate validation reports for de-identification quality.

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
