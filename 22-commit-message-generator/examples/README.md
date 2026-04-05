# Examples for Commit Message Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`generate_commit_messages()`** — Generate conventional commit messages from a diff.
- **`generate_batch_messages()`** — Generate commit messages for multiple diffs (batch mode).

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
