# Examples for Stress Management Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`show_disclaimer()`** — Display the mental health disclaimer.
- **`run_breathing_exercise()`** — Run a guided breathing exercise with timed progress bars.
- **`calculate_stress_score()`** — Calculate a detailed stress score from assessment answers.
- **`get_cbt_worksheet()`** — Return a CBT worksheet template by type.
- **`get_coping_suggestions()`** — Return coping suggestions appropriate for the given stress severity.

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
