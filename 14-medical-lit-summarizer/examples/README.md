# Examples for Medical Lit Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`extract_section()`** — Extract a specific section from a paper using the LLM.
- **`summarize_paper()`** — Summarize a medical paper into structured sections.
- **`extract_pico()`** — Extract PICO framework elements from a medical paper.
- **`rate_evidence_quality()`** — Rate the quality of evidence in a medical paper.
- **`format_citation()`** — Format a citation for the paper in the specified style.

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
