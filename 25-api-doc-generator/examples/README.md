# Examples for Api Doc Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`generate_docs()`** — Generate API documentation for all files in the source path.
- **`generate_openapi()`** — Generate OpenAPI specification from source code.
- **`export_docs()`** — Export documentation to file.

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
