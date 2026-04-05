# Examples for Health Plan Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml, falling back to defaults.
- **`get_milestones_for_goal()`** — Get milestones for a given goal.
- **`generate_adaptive_recommendation()`** — Generate adaptive recommendations based on progress.
- **`generate_plan()`** — Generate a wellness plan using the LLM.
- **`start_plan()`** — Initialize tracking for a new plan.
- **`ProgressTracker`** — Track progress toward health goals.

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
