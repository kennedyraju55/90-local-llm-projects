# Examples for Gdpr Compliance Checker

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`check_compliance()`** — Check content for GDPR compliance using LLM.
- **`generate_checklist()`** — Generate a GDPR compliance checklist using LLM.
- **`build_article_checklist()`** — Build an article-by-article compliance checklist from content analysis.
- **`map_data_flows()`** — Extract data flow mappings from document content.
- **`generate_dpo_recommendations()`** — Generate DPO recommendations based on checklist results.
- **`ComplianceStatus`** — Use ComplianceStatus
- **`ChecklistItem`** — A single GDPR compliance checklist item.
- **`DataFlowEntry`** — A data flow mapping entry.

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
