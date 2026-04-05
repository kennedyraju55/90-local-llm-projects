# Examples for Code Complexity Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`calculate_cyclomatic_complexity()`** — Calculate cyclomatic complexity for a function/method node.
- **`calculate_cognitive_complexity()`** — Calculate cognitive complexity (simplified) for a function node.
- **`count_lines()`** — Count different types of lines in source code.
- **`calculate_halstead_volume()`** — Estimate Halstead volume (simplified).

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
