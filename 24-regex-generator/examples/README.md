# Examples for Regex Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`generate_regex()`** — Generate a regex pattern from natural language description.
- **`explain_regex()`** — Explain an existing regex pattern in plain English.
- **`get_pattern_from_library()`** — Look up a pattern from the built-in pattern library.
- **`list_library_patterns()`** — Return the full pattern library.

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
