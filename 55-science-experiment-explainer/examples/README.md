# Examples for Science Experiment Explainer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`setup_logging()`** — Configure the root logger based on config values.
- **`parse_response()`** — Parse an LLM response that may be wrapped in markdown code fences.
- **`explain_experiment()`** — Generate an experiment explanation via the LLM.
- **`suggest_alternatives()`** — Ask the LLM for alternative experiments related to the given one.
- **`search_experiments()`** — Search for experiments matching the given criteria via the LLM.
- **`ConfigManager`** — Loads and provides access to config.yaml values.
- **`DifficultyRating`** — Use DifficultyRating
- **`Material`** — Use Material

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
