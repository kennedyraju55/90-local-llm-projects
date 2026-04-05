# Examples for Incident Report Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`generate_report()`** — Generate an incident report from raw logs.
- **`generate_timeline()`** — Extract a timeline from incident logs.
- **`build_timeline()`** — Parse logs into structured timeline entries.
- **`calculate_impact()`** — Calculate impact assessment from incident data.
- **`generate_lessons_learned()`** — Generate lessons learned from an incident.
- **`Priority`** — Use Priority
- **`TimelineEntry`** — A single event in an incident timeline.
- **`ImpactAssessment`** — Impact assessment for an incident.

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
