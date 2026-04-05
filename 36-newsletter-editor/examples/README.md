# Examples for Newsletter Editor

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file with defaults.
- **`read_input_file()`** — Read raw notes/content from a file.
- **`get_section_templates()`** — Return available section templates.
- **`get_subscriber_segments()`** — Return available subscriber segments.
- **`build_prompt()`** — Build the newsletter generation prompt.

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
