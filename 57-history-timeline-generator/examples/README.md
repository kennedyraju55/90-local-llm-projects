# Examples for History Timeline Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Call load_config
- **`generate_timeline()`** — Generate a historical timeline using the LLM.
- **`get_figure_profiles()`** — Get detailed profiles of key historical figures.
- **`get_cause_effect_chains()`** — Analyze cause-and-effect chains for a historical topic.
- **`check_service()`** — Call check_service
- **`HistoricalEvent`** — Use HistoricalEvent
- **`KeyFigureProfile`** — Use KeyFigureProfile
- **`CauseEffectChain`** — Use CauseEffectChain

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
