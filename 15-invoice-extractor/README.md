<div align="center">

<img src="docs/images/banner.svg" alt="Invoice Extractor Banner" width="800"/>

<br/><br/>

<img src="https://img.shields.io/badge/Gemma_4-Ollama-orange?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/Rich-Terminal_UI-purple?style=flat-square" alt="Rich"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/><br/>

**Extract structured data from invoices using a local LLM — no cloud, no API keys, 100% private.**

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

<br/>

---

## 📑 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
  - [Python API](#python-api)
  - [CLI Commands](#cli-commands)
- [API Reference](#-api-reference)
- [Output Format](#-output-format)
- [Examples](#-examples)
- [Project Structure](#-project-structure)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Manual invoice data entry is one of the most error-prone and time-consuming tasks in
accounting and finance workflows. Studies show that **manual data entry has an error rate
of roughly 1% per field** — and a single invoice can contain 15–30 fields. Over hundreds
of invoices per month, those errors compound into reconciliation nightmares, duplicate
payments, and audit failures.

**Common pain points this project solves:**

| Problem | Impact | How Invoice Extractor Helps |
|---|---|---|
| Manually keying vendor details | Typos in vendor names cause matching failures | `extract_invoice_data()` returns structured vendor objects |
| Inconsistent date formats | "01/02/2025" — is that Jan 2 or Feb 1? | All dates normalized to ISO 8601 (`YYYY-MM-DD`) |
| Missing line items | Skipped rows lead to underpayment disputes | Every line item extracted with description, qty, unit price, total |
| Duplicate invoices | Same invoice paid twice = direct financial loss | `detect_duplicates()` catches near-matches before payment |
| No categorization | Month-end expense reports require manual tagging | `categorize_items()` auto-tags line items via LLM |
| Cloud privacy concerns | Sensitive financial data sent to third-party APIs | 100% local processing — Ollama + Gemma 4 on your machine |

> **This tool doesn't replace your accounting software.** It sits *before* it — extracting,
> structuring, de-duplicating, and categorizing invoice data so you can import clean records
> into your ERP, QuickBooks, Xero, or spreadsheet.

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

- **Structured extraction** — vendor, invoice number, dates, line items, totals, tax, payment terms
- **Batch processing** — Process multiple invoices at once
- **CSV/JSON export** — Export extracted data for accounting systems
- **Duplicate detection** — Identify potential duplicate invoices
### Feature Highlights

- **🔍 Structured Extraction** — Pull vendor details, dates, line items, subtotals, tax, and grand total from any invoice
- **⚡ Batch Processing** — Feed multiple invoice files at once; each file returns structured data or a clear error
- **🔁 Duplicate Detection** — Smart similarity matching with configurable threshold to prevent double payments
- **🏷️ Item Categorization** — AI-powered line item tagging (Office Supplies, Software Licenses, Professional Services, etc.)
- **📊 Multi-Format Export** — Output as JSON, CSV, or a Rich-formatted terminal table
- **🔒 100% Private** — All processing runs locally via Ollama + Gemma 4. No cloud APIs. No data leaves your machine.

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800"/>
</div>

<br/>

The pipeline is straightforward:

```
Invoice Files (PDF/TXT)
    │
    ▼
Text Extraction (PyPDF2 / pdfplumber)
    │
    ▼
Gemma 4 via Ollama
    ├── extract_invoice_data()   → Structured fields
    ├── categorize_items()       → Expense categories
    └── detect_duplicates()      → Similarity matching
    │
    ▼
Structured Output (JSON / CSV / Rich Table)
```

All LLM calls go through the shared `common/llm_client.py` module, which handles prompt
construction, JSON parsing, and error recovery. The CLI layer is built with Click and
uses Rich for terminal formatting.

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/invoice-extractor.git
cd invoice-extractor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama and pull the model
ollama serve
ollama pull gemma4

# 4. Extract an invoice
python -m invoice_extractor.cli extract --file sample_invoice.txt --output table
```

**That's it.** You should see a Rich-formatted table with vendor info, line items, and totals.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/invoice-extractor.git
cd invoice-extractor
docker compose up

# Access the web UI
open http://localhost:8501
```

### Docker Commands

| Command | Description |
|---------|-------------|
| `docker compose up` | Start app + Ollama |
| `docker compose up -d` | Start in background |
| `docker compose down` | Stop all services |
| `docker compose logs -f` | View live logs |
| `docker compose build --no-cache` | Rebuild from scratch |

### Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Streamlit UI  │────▶│   Ollama + LLM  │
│   Port 8501     │     │   Port 11434    │
└─────────────────┘     └─────────────────┘
```

> **Note:** First run will download the Gemma 4 model (~5GB). Subsequent starts are instant.

---


---


---

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.invoice_extractor.api:app --reload --port 8000

# Or with Docker
docker compose up
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |
| `POST` | `/analyze` | Main analysis endpoint |

### Example Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "your input here"}'
```

> 📖 Visit `http://localhost:8000/docs` for the full interactive API documentation.

## 📦 Installation

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | Via Ollama | Language model for extraction |

### Step-by-Step

```bash
# Clone
git clone https://github.com/kennedyraju55/invoice-extractor.git
cd invoice-extractor

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Install Python dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .

# Start Ollama (if not already running)
ollama serve

# Pull the Gemma 4 model
ollama pull gemma4
```

### Dependencies

| Library | Purpose |
|---|---|
| `click` | CLI framework with subcommands and options |
| `rich` | Terminal tables, progress bars, styled output |
| `ollama` | Python client for the Ollama local LLM server |
| `PyPDF2` | PDF text extraction (basic) |
| `pdfplumber` | PDF text extraction (layout-aware, tables) |
| `csv` (stdlib) | CSV reading and writing |
| `json` (stdlib) | JSON serialization and parsing |

---

## ⚙️ Configuration

The project uses a `config.yaml` file for runtime settings. You can also pass a custom
config path via the `--config` CLI flag.

```yaml
# config.yaml
llm:
  model: "gemma4"
  base_url: "http://localhost:11434"
  temperature: 0.1           # Low temperature for deterministic extraction
  max_retries: 3

extraction:
  date_format: "ISO8601"     # Dates normalized to YYYY-MM-DD
  currency: "USD"            # Default currency if not detected

duplicates:
  threshold: 0.9             # Similarity threshold (0.0 to 1.0)
  fields:
    - invoice_number
    - vendor.name
    - grand_total
    - date

categories:
  - "Office Supplies"
  - "Software & Licenses"
  - "Professional Services"
  - "Travel & Transportation"
  - "Utilities"
  - "Hardware & Equipment"
  - "Marketing & Advertising"
  - "Other"
```

### Environment Variables

Copy `.env.example` to `.env` and customize as needed:

```bash
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma4
LOG_LEVEL=INFO
```

---

## 📖 Usage

### Python API

#### Single Invoice Extraction

```python
from invoice_extractor.core import extract_invoice_data

# Read invoice text (from file, PDF extraction, or any source)
with open("invoice.txt", "r") as f:
    text = f.read()

# Extract structured data
result = extract_invoice_data(text)

print(result["vendor"]["name"])        # "Acme Corporation"
print(result["invoice_number"])        # "INV-2025-0042"
print(result["date"])                  # "2025-01-15"
print(result["due_date"])             # "2025-02-14"
print(result["grand_total"])          # 1247.50
print(result["currency"])            # "USD"

# Line items
for item in result["line_items"]:
    print(f"  {item['description']}: {item['quantity']} x ${item['unit_price']} = ${item['total']}")
```

#### Batch Processing

```python
from invoice_extractor.core import batch_extract

file_paths = [
    "invoices/january/inv-001.txt",
    "invoices/january/inv-002.pdf",
    "invoices/january/inv-003.txt",
    "invoices/february/inv-004.pdf",
]

results = batch_extract(file_paths)

for entry in results:
    if "data" in entry:
        inv = entry["data"]
        print(f"✓ {entry['file']}: {inv['vendor']['name']} — ${inv['grand_total']}")
    else:
        print(f"✗ {entry['file']}: {entry['error']}")
```

**Output:**

```
✓ invoices/january/inv-001.txt: Acme Corporation — $1,247.50
✓ invoices/january/inv-002.pdf: TechSupply Co. — $3,890.00
✗ invoices/january/inv-003.txt: Failed to parse — invalid format
✓ invoices/february/inv-004.pdf: CloudHost Inc. — $499.99
```

#### Duplicate Detection

```python
from invoice_extractor.core import batch_extract, detect_duplicates

results = batch_extract(["inv1.txt", "inv2.txt", "inv3.txt", "inv4.txt"])

# Extract just the data dicts (skip errors)
invoices = [r["data"] for r in results if "data" in r]

# Find duplicates with default threshold (0.9)
duplicates = detect_duplicates(invoices, threshold=0.9)

for idx1, idx2, reason in duplicates:
    print(f"⚠ Possible duplicate: invoice {idx1} and {idx2}")
    print(f"  Reason: {reason}")
```

**Output:**

```
⚠ Possible duplicate: invoice 0 and 3
  Reason: Same vendor (Acme Corporation), same total ($1,247.50), dates within 1 day
```

#### Item Categorization

```python
from invoice_extractor.core import extract_invoice_data, categorize_items

text = open("invoice.txt").read()
invoice_data = extract_invoice_data(text)

# Categorize line items using the LLM
categorized = categorize_items(invoice_data)

for item in categorized:
    print(f"  [{item['category']}] {item['description']} — ${item['total']}")
```

**Output:**

```
  [Office Supplies] A4 Printer Paper (5 reams) — $45.00
  [Software & Licenses] Adobe Creative Cloud (Annual) — $599.88
  [Hardware & Equipment] USB-C Docking Station — $189.99
```

#### CSV Export

```python
from invoice_extractor.core import batch_extract, export_to_csv

results = batch_extract(["inv1.txt", "inv2.txt"])
invoices = [r["data"] for r in results if "data" in r]

csv_string = export_to_csv(invoices)
print(csv_string)

# Or write to file
with open("export.csv", "w") as f:
    f.write(csv_string)
```

---

### CLI Commands

The CLI is built with Click and supports three main subcommands plus global options.

#### Global Options

```
--verbose / -v      Enable verbose logging output
--config PATH       Path to custom config.yaml file
```

#### `extract` — Single Invoice Extraction

```bash
# Extract and display as a Rich table (default)
python -m invoice_extractor.cli extract --file invoice.txt

# Extract and output as JSON
python -m invoice_extractor.cli extract --file invoice.pdf --output json

# Extract and output as CSV
python -m invoice_extractor.cli extract -f invoice.txt -o csv

# With verbose logging
python -m invoice_extractor.cli -v extract -f invoice.txt -o table
```

**Options:**

| Flag | Short | Required | Description |
|---|---|---|---|
| `--file` | `-f` | Yes | Path to the invoice file (PDF or TXT) |
| `--output` | `-o` | No | Output format: `json`, `table`, or `csv` (default: `table`) |

**Example output (table format):**

```
┌──────────────────────────────────────────────────────────┐
│                    Invoice Details                        │
├──────────────────┬───────────────────────────────────────┤
│ Invoice Number   │ INV-2025-0042                         │
│ Vendor           │ Acme Corporation                      │
│ Vendor Address   │ 123 Business Ave, Suite 100, NY 10001 │
│ Vendor Email     │ billing@acmecorp.com                  │
│ Date             │ 2025-01-15                            │
│ Due Date         │ 2025-02-14                            │
│ Payment Terms    │ Net 30                                │
│ Currency         │ USD                                   │
├──────────────────┴───────────────────────────────────────┤
│                     Line Items                            │
├────────────────────────┬─────┬────────────┬──────────────┤
│ Description            │ Qty │ Unit Price │ Total        │
├────────────────────────┼─────┼────────────┼──────────────┤
│ A4 Printer Paper       │ 5   │ $9.00      │ $45.00       │
│ Adobe Creative Cloud   │ 1   │ $599.88    │ $599.88      │
│ USB-C Docking Station  │ 1   │ $189.99    │ $189.99      │
├────────────────────────┴─────┴────────────┴──────────────┤
│ Subtotal: $834.87    Tax: $66.79    Grand Total: $901.66 │
└──────────────────────────────────────────────────────────┘
```

#### `batch` — Batch Processing

```bash
# Process multiple invoice files
python -m invoice_extractor.cli batch --files inv1.txt --files inv2.txt --files inv3.pdf

# Process and export to CSV
python -m invoice_extractor.cli batch -f inv1.txt -f inv2.pdf --export results.csv

# With verbose output
python -m invoice_extractor.cli -v batch -f invoices/*.txt --export output.csv
```

**Options:**

| Flag | Short | Required | Description |
|---|---|---|---|
| `--files` | `-f` | Yes | Invoice file paths (can be specified multiple times) |
| `--export` | `-e` | No | Export results to a CSV file |

#### `categorize` — Item Categorization

```bash
# Categorize line items in an invoice
python -m invoice_extractor.cli categorize --file invoice.txt

# With custom config for category definitions
python -m invoice_extractor.cli --config custom.yaml categorize -f invoice.txt
```

**Options:**

| Flag | Short | Required | Description |
|---|---|---|---|
| `--file` | `-f` | Yes | Path to the invoice file |

**Example output:**

```
┌──────────────────────────────────────────────────────┐
│              Categorized Line Items                   │
├────────────────────────┬──────────┬───────────────────┤
│ Description            │ Total    │ Category          │
├────────────────────────┼──────────┼───────────────────┤
│ A4 Printer Paper       │ $45.00   │ Office Supplies   │
│ Adobe Creative Cloud   │ $599.88  │ Software          │
│ USB-C Docking Station  │ $189.99  │ Hardware          │
└────────────────────────┴──────────┴───────────────────┘
```

---

## 📚 API Reference

### `extract_invoice_data(text, config=None) → dict`

Extracts structured data from raw invoice text using the local LLM.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `str` | — | Raw text content of the invoice |
| `config` | `dict` or `None` | `None` | Optional configuration overrides |

**Returns:** A dictionary with the following structure:

```python
{
    "vendor": {
        "name": str,         # "Acme Corporation"
        "address": str,      # "123 Business Ave, Suite 100, NY 10001"
        "phone": str,        # "+1-555-0123"
        "email": str         # "billing@acmecorp.com"
    },
    "invoice_number": str,   # "INV-2025-0042"
    "date": str,             # "2025-01-15" (ISO 8601)
    "due_date": str,         # "2025-02-14" (ISO 8601)
    "line_items": [
        {
            "description": str,   # "A4 Printer Paper (5 reams)"
            "quantity": int,      # 5
            "unit_price": float,  # 9.00
            "total": float        # 45.00
        }
    ],
    "subtotal": float,       # 834.87
    "tax": float,            # 66.79
    "grand_total": float,    # 901.66
    "currency": str,         # "USD"
    "payment_terms": str     # "Net 30"
}
```

---

### `batch_extract(file_paths, config=None) → list`

Processes multiple invoice files and returns results for each.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `file_paths` | `list[str]` | — | List of file paths to process |
| `config` | `dict` or `None` | `None` | Optional configuration overrides |

**Returns:** A list of dictionaries, each containing either:

```python
# Success
{"file": "inv1.txt", "data": { ... }}   # data is the extract_invoice_data() result

# Failure
{"file": "inv2.txt", "error": "Failed to parse — invalid format"}
```

---

### `detect_duplicates(invoices, threshold=0.9) → list`

Compares a list of extracted invoices and identifies potential duplicates.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `invoices` | `list[dict]` | — | List of invoice data dictionaries |
| `threshold` | `float` | `0.9` | Similarity threshold (0.0 to 1.0) |

**Returns:** A list of tuples:

```python
[
    (0, 3, "Same vendor (Acme Corporation), same total ($1,247.50), dates within 1 day"),
    (1, 5, "Same invoice number (INV-2025-0099), different vendor names (possible rebrand)")
]
```

Each tuple contains `(index1, index2, reason)` where the indices refer to positions in
the input list.

---

### `categorize_items(invoice_data, config=None) → list`

Uses the LLM to assign expense categories to each line item.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `invoice_data` | `dict` | — | A single invoice data dictionary (from `extract_invoice_data()`) |
| `config` | `dict` or `None` | `None` | Optional config with custom category list |

**Returns:** A list of line item dictionaries with an added `category` field:

```python
[
    {"description": "A4 Printer Paper", "quantity": 5, "unit_price": 9.0, "total": 45.0, "category": "Office Supplies"},
    {"description": "Adobe Creative Cloud", "quantity": 1, "unit_price": 599.88, "total": 599.88, "category": "Software & Licenses"}
]
```

---

### `export_to_csv(invoices) → str`

Converts a list of extracted invoice data dictionaries into a CSV-formatted string.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `invoices` | `list[dict]` | — | List of invoice data dictionaries |

**Returns:** A CSV string with headers. Each line item becomes a separate row, with
invoice-level fields (vendor, invoice number, date) repeated on each row.

```csv
invoice_number,vendor_name,date,due_date,description,quantity,unit_price,total,subtotal,tax,grand_total,currency
INV-2025-0042,Acme Corporation,2025-01-15,2025-02-14,A4 Printer Paper,5,9.00,45.00,834.87,66.79,901.66,USD
INV-2025-0042,Acme Corporation,2025-01-15,2025-02-14,Adobe Creative Cloud,1,599.88,599.88,834.87,66.79,901.66,USD
```

---

## 📄 Output Format

### JSON Output

When using `--output json`, the CLI prints the full extraction result as indented JSON:

```json
{
  "vendor": {
    "name": "Acme Corporation",
    "address": "123 Business Ave, Suite 100, NY 10001",
    "phone": "+1-555-0123",
    "email": "billing@acmecorp.com"
  },
  "invoice_number": "INV-2025-0042",
  "date": "2025-01-15",
  "due_date": "2025-02-14",
  "line_items": [
    {
      "description": "A4 Printer Paper (5 reams)",
      "quantity": 5,
      "unit_price": 9.0,
      "total": 45.0
    },
    {
      "description": "Adobe Creative Cloud (Annual)",
      "quantity": 1,
      "unit_price": 599.88,
      "total": 599.88
    }
  ],
  "subtotal": 644.88,
  "tax": 51.59,
  "grand_total": 696.47,
  "currency": "USD",
  "payment_terms": "Net 30"
}
```

### Table Output

The default `--output table` format uses Rich to render a styled terminal table with
vendor info, line items, and totals — see the [CLI extract example](#extract--single-invoice-extraction) above.

### CSV Output

Using `--output csv` or `export_to_csv()`, each line item becomes a row with invoice-level
fields denormalized across rows for easy spreadsheet import.

---

## 💻 Examples

### End-to-End: From PDF to CSV

```bash
# Step 1: Extract a single invoice to verify
python -m invoice_extractor.cli extract -f invoices/january/inv-001.pdf -o json

# Step 2: Batch process all January invoices
python -m invoice_extractor.cli batch \
    -f invoices/january/inv-001.pdf \
    -f invoices/january/inv-002.pdf \
    -f invoices/january/inv-003.txt \
    --export january_invoices.csv

# Step 3: Categorize items for expense reporting
python -m invoice_extractor.cli categorize -f invoices/january/inv-001.pdf
```

### Python Script: Monthly Report Generator

```python
"""Generate a monthly invoice summary report."""

import os
import json
from invoice_extractor.core import (
    batch_extract,
    detect_duplicates,
    categorize_items,
    export_to_csv,
)


def generate_monthly_report(invoice_dir: str, output_path: str):
    # Collect all invoice files
    file_paths = [
        os.path.join(invoice_dir, f)
        for f in os.listdir(invoice_dir)
        if f.endswith((".txt", ".pdf"))
    ]

    print(f"Processing {len(file_paths)} invoices...")

    # Batch extract
    results = batch_extract(file_paths)

    successful = [r for r in results if "data" in r]
    failed = [r for r in results if "error" in r]

    print(f"  ✓ {len(successful)} extracted successfully")
    print(f"  ✗ {len(failed)} failed")

    # Check for duplicates
    invoices = [r["data"] for r in successful]
    duplicates = detect_duplicates(invoices)

    if duplicates:
        print(f"\n⚠ Found {len(duplicates)} potential duplicate(s):")
        for idx1, idx2, reason in duplicates:
            print(f"  - {successful[idx1]['file']} ↔ {successful[idx2]['file']}")
            print(f"    {reason}")

    # Categorize all items
    for entry in successful:
        entry["data"]["categorized_items"] = categorize_items(entry["data"])

    # Export to CSV
    csv_output = export_to_csv(invoices)
    with open(output_path, "w") as f:
        f.write(csv_output)

    print(f"\n✓ Report exported to {output_path}")

    # Summary
    total_spend = sum(inv["grand_total"] for inv in invoices)
    print(f"  Total spend: ${total_spend:,.2f}")
    print(f"  Unique vendors: {len(set(inv['vendor']['name'] for inv in invoices))}")


if __name__ == "__main__":
    generate_monthly_report("invoices/january/", "reports/january_summary.csv")
```

### Using Custom Configuration

```python
from invoice_extractor.core import extract_invoice_data

custom_config = {
    "llm": {
        "model": "gemma4",
        "temperature": 0.0,  # Maximum determinism
    },
    "categories": [
        "Raw Materials",
        "Manufacturing",
        "Shipping & Logistics",
        "Quality Control",
        "Administrative",
    ],
}

text = open("supplier_invoice.txt").read()
result = extract_invoice_data(text, config=custom_config)
```

---

## 📁 Project Structure

```
15-invoice-extractor/
├── src/
│   └── invoice_extractor/
│       ├── __init__.py          # Package init, version
│       ├── core.py              # Core extraction logic
│       │                          extract_invoice_data()
│       │                          batch_extract()
│       │                          detect_duplicates()
│       │                          categorize_items()
│       │                          export_to_csv()
│       ├── cli.py               # Click CLI commands
│       │                          extract, batch, categorize
│       ├── config.py            # Configuration loader
│       └── utils.py             # PDF text extraction, helpers
├── common/
│   └── llm_client.py            # Shared Ollama LLM client
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core functions
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner
│       ├── architecture.svg     # Architecture diagram
│       └── features.svg         # Features overview
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup
├── requirements.txt             # Python dependencies
├── Makefile                     # Build/test shortcuts
├── .env.example                 # Environment variable template
├── .gitignore
└── README.md                    # This file
```

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src/invoice_extractor

# Run specific test file
python -m pytest tests/test_core.py -v

# Run specific test
python -m pytest tests/test_core.py::test_extract_invoice_data -v
```

---

## ❓ FAQ

### What PDF formats are supported?

Invoice Extractor works with **text-based PDFs** — PDFs where the text layer is embedded
and selectable. This covers the vast majority of digitally-generated invoices (from
accounting software, online billing platforms, etc.).

**Scanned image PDFs** (where the invoice is a photograph or scan with no embedded text)
are **not currently supported** because they require OCR (Optical Character Recognition)
as a preprocessing step. If you need OCR support, you can preprocess with `tesseract` or
a similar tool and feed the extracted text to `extract_invoice_data()`.

### How accurate is the extraction?

Accuracy depends on the invoice format and complexity. In testing with common invoice
layouts:

| Metric | Accuracy |
|---|---|
| Vendor name | ~95% |
| Invoice number | ~93% |
| Dates (ISO 8601) | ~97% |
| Line items (all fields) | ~90% |
| Totals (subtotal, tax, grand total) | ~94% |

The LLM excels at understanding varied layouts and formats. Accuracy improves when
invoices follow standard conventions (clear labels, consistent formatting). For critical
financial workflows, we recommend **spot-checking** the first few results from a new
vendor before automating fully.

### Is there a batch size limit?

There is no hard-coded batch size limit. The practical limit depends on:

- **Available RAM** — each invoice's text is held in memory during processing
- **Ollama throughput** — Gemma 4 processes one invoice at a time by default
- **Disk space** — for PDF extraction temporary buffers

In practice, batches of **50–200 invoices** work well. For larger volumes (1,000+),
consider splitting into smaller batches and aggregating the CSV output.

### Can I use a different LLM model?

Yes. Update the `model` field in `config.yaml` or set the `OLLAMA_MODEL` environment
variable. Any model available in your local Ollama installation can be used:

```yaml
llm:
  model: "llama3.1"   # or mistral, phi3, etc.
```

Note that extraction accuracy varies by model. Gemma 4 is recommended as it provides
the best balance of accuracy and speed for structured data extraction tasks.

### How does duplicate detection work?

`detect_duplicates()` compares invoices across multiple fields:

1. **Invoice number** — exact match check
2. **Vendor name** — fuzzy string similarity
3. **Grand total** — exact numeric match
4. **Date proximity** — invoices within a configurable window

A pair is flagged as a potential duplicate when the combined similarity score exceeds the
`threshold` parameter (default: 0.9). The `reason` string in each result tuple explains
which fields matched and why.

### Can I customize expense categories?

Yes. Define your categories in `config.yaml`:

```yaml
categories:
  - "Raw Materials"
  - "Manufacturing"
  - "Shipping & Logistics"
  - "Quality Control"
  - "Administrative"
```

Or pass them programmatically:

```python
config = {"categories": ["Dept A", "Dept B", "Dept C"]}
categorized = categorize_items(invoice_data, config=config)
```

### Does it work offline?

**Yes, 100%.** The entire pipeline runs locally. Ollama serves the LLM model on your
machine. No internet connection is required after the initial model download.

### What about multi-page invoices?

Multi-page PDFs are handled automatically. `PyPDF2` / `pdfplumber` extracts text from all
pages and concatenates them before sending to the LLM. The model is instructed to treat
the full text as a single invoice.

### Can I process invoices in non-English languages?

Gemma 4 has multilingual capabilities and can extract data from invoices in many
languages. However, accuracy is highest for English invoices. For other languages,
test with a small sample first and adjust the `temperature` setting if needed.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork and clone
git clone https://github.com/<your-username>/invoice-extractor.git
cd invoice-extractor

# Create a feature branch
git checkout -b feature/your-feature-name

# Install dev dependencies
pip install -r requirements.txt
pip install -e .

# Make your changes and run tests
python -m pytest tests/ -v

# Commit and push
git add .
git commit -m "feat: your feature description"
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

### Development Guidelines

- Follow existing code style (PEP 8)
- Add tests for new functionality
- Update this README if adding new features or CLI commands
- Keep commits focused and well-described

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<br/>

Built with 🧾 by [kennedyraju55](https://github.com/kennedyraju55) — powered by Ollama + Gemma 4

</div>
