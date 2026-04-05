# Examples for Quiz Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`setup_logging()`** — Configure the quiz_gen logger.
- **`parse_response()`** — Parse LLM response text into a quiz dict, handling code fences.
- **`validate_quiz_data()`** — Return a list of validation errors (empty == valid).
- **`generate_quiz()`** — Generate a quiz using the LLM.
- **`score_quiz()`** — Score user answers against the quiz and return a QuizResult.
- **`ConfigManager`** — Loads and provides access to config.yaml with sensible defaults.
- **`DifficultyLevel`** — Use DifficultyLevel
- **`QuizQuestion`** — Use QuizQuestion

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
