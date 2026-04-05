# Examples for Policy Compliance Checker

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`read_file()`** — Read and return the contents of a file.
- **`check_compliance()`** — Send document and policy to the LLM for compliance analysis.
- **`parse_compliance_response()`** — Parse the LLM JSON response into a compliance report dict.
- **`filter_violations()`** — Filter violations by severity level.
- **`get_score_color()`** — Get the display color for a compliance score.

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
