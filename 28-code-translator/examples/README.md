# Examples for Code Translator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`detect_source_language()`** — Detect the source language from file extension.
- **`get_language_name()`** — Get display name for a language code.
- **`get_language_ext()`** — Get file extension for a language code.
- **`read_source_file()`** — Read the source code file.

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
