# Examples for Docker Compose Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from config.yaml.
- **`get_service_catalog()`** — Return the full service catalog organized by category.
- **`get_flat_catalog()`** — Return a flat dictionary of all services.
- **`get_env_profile()`** — Return configuration profile for an environment.
- **`generate_compose()`** — Generate a Docker Compose file from a stack description.

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
