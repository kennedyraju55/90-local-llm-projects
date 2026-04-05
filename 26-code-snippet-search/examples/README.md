# Examples for Code Snippet Search

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`get_file_hash()`** — Compute MD5 hash of a file for cache invalidation.
- **`detect_language()`** — Detect programming language from file extension.
- **`scan_directory()`** — Scan a directory and read code files with metadata.
- **`build_search_context()`** — Build a combined context from files for the LLM.

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
