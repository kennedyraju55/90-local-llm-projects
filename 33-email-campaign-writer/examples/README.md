# Examples for Email Campaign Writer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load and cache application configuration from config.yaml.
- **`setup_logging()`** — Configure logging from config.yaml.
- **`build_prompt()`** — Build the email campaign generation prompt.
- **`generate_campaign()`** — Generate an email campaign using the LLM and return raw text.
- **`generate_subject_variants()`** — Generate A/B subject-line variants for testing.
- **`Email`** — Represents a single email in a campaign sequence.
- **`Campaign`** — Represents a full email campaign.

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
