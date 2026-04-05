# Examples for Veterinary Advisor Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`format_pet_context()`** — Format pet profile into context string.
- **`get_response()`** — Get a response from the vet advisor bot.
- **`check_symptoms()`** — Check symptoms and provide guidance.
- **`get_breed_advice()`** — Get breed-specific care advice.
- **`get_nutrition_advice()`** — Get nutrition advice for a specific pet.

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
