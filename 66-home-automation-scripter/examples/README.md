# Examples for Home Automation Scripter

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file, falling back to defaults.
- **`load_rules()`** — Load saved automation rules from JSON.
- **`save_rule()`** — Persist a new automation rule and return it with id/timestamp.
- **`delete_rule()`** — Delete a rule by its integer id. Returns True if found and deleted.
- **`validate_script()`** — Validate an automation script for a given platform.

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
