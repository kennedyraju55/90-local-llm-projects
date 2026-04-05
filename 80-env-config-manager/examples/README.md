# Examples for Env Config Manager

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load application configuration from config.yaml.
- **`parse_env_file()`** — Parse a .env file into key-value pairs.
- **`detect_secrets()`** — Detect potential secrets in environment variables.
- **`compare_envs()`** — Compare two environment configurations.
- **`generate_migration_script()`** — Generate a migration script between environments.

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
