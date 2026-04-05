# Examples for Log File Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`read_log_file()`** — Read a log file, optionally only the last N lines.
- **`analyze_logs()`** — Analyze log content using the LLM.
- **`cluster_errors()`** — Cluster similar errors using LLM.
- **`match_patterns()`** — Match known patterns in log content.
- **`detect_anomalies()`** — Detect anomalies in log content.
- **`LogLevel`** — Use LogLevel
- **`PatternMatch`** — A matched log pattern.
- **`ErrorCluster`** — A cluster of similar errors.

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
