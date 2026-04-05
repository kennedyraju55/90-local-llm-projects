# Examples for Invoice Extractor

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`extract_invoice_data()`** — Send invoice text to the LLM and parse the structured JSON response.
- **`batch_extract()`** — Extract data from multiple invoice files.
- **`detect_duplicates()`** — Detect potential duplicate invoices by invoice number and vendor.
- **`categorize_items()`** — Categorize invoice line items using the LLM.
- **`export_to_csv()`** — Export extracted invoice data to CSV format string.

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
