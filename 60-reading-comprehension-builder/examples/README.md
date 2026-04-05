# Examples for Reading Comprehension Builder

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Call load_config
- **`generate_comprehension()`** — Generate a reading comprehension exercise using the LLM.
- **`score_exercise()`** — Score a completed exercise and return detailed results.
- **`get_answer_key()`** — Get the answer key with explanations.
- **`check_service()`** — Call check_service
- **`VocabularyWord`** — Use VocabularyWord
- **`Question`** — Use Question
- **`ScoringRubric`** — Use ScoringRubric

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
