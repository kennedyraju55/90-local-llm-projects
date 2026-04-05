# Examples for Cybersecurity Alert Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`summarize_alert()`** — Summarize a security alert using the LLM.
- **`prioritize_alerts()`** — Prioritize multiple alerts by risk level.
- **`extract_iocs()`** — Extract Indicators of Compromise from alert text.
- **`lookup_cve()`** — Look up CVE information from the local database.
- **`extract_cves()`** — Extract and look up all CVE identifiers from text.
- **`Severity`** — Use Severity
- **`IOCResult`** — Indicator of Compromise extraction result.
- **`CVEInfo`** — CVE database lookup result.

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
