# Examples for Exercise Form Guide

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`get_warmup_routine()`** — Return a list of warm-up exercises for the given muscle group.
- **`get_cooldown_routine()`** — Return a list of cool-down stretches for the given muscle group.
- **`get_exercise_variations()`** — Return the progression path for a given exercise.
- **`get_muscle_info()`** — Return muscle group information from the database.
- **`generate_guide()`** — Generate a detailed exercise form guide using the LLM.

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
