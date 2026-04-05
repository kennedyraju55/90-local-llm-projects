# Examples for Unit Test Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`extract_code_info()`** — Extract functions, classes, and imports from a Python file.
- **`analyze_coverage()`** — Analyze what needs testing and estimate coverage requirements.
- **`generate_tests()`** — Generate unit tests for the code in filepath.
- **`organize_test_structure()`** — Suggest test file organization.

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
