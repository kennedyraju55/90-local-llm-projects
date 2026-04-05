# Examples for Infra Doc Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from config.yaml.
- **`detect_config_type()`** — Detect the type of infrastructure config file.
- **`extract_dependencies()`** — Extract service/resource dependencies from config content.
- **`generate_docs()`** — Generate documentation from an infrastructure config file.
- **`generate_diagram()`** — Generate an architecture diagram description.

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
