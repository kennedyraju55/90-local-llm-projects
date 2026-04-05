# Examples for Stack Trace Explainer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`explain_trace()`** — Analyze a stack trace and return explanation.
- **`generate_fix_code()`** — Generate fix code based on trace and explanation.
- **`find_similar_errors()`** — Find similar errors and distinguish between them.

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
