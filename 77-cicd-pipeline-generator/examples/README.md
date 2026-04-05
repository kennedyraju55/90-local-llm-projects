# Examples for Cicd Pipeline Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from config.yaml.
- **`get_platforms()`** — Return all supported CI/CD platforms.
- **`get_stage_catalog()`** — Return available pipeline stages.
- **`get_secret_template()`** — Return secret templates for a platform.
- **`get_matrix_preset()`** — Return matrix build preset for a language.

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
