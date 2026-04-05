# Examples for Legal Doc Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`summarize_document()`** — Send document text to the LLM for analysis and summarization.
- **`extract_clauses()`** — Extract and categorize individual clauses from a legal document.
- **`score_risks()`** — Analyze document for risk factors and return risk scores.
- **`compare_documents()`** — Compare multiple legal documents side by side.
- **`generate_export_markdown()`** — Generate PDF-ready markdown export combining all analyses.

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
