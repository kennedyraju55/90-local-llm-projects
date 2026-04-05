# Examples for Essay Grader

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`setup_logging()`** — Configure logging for the application.
- **`calculate_grade_letter()`** — Convert a numeric score to a letter grade.
- **`parse_response()`** — Parse an LLM JSON response, stripping markdown fences if present.
- **`validate_grade_data()`** — Validate grade data structure. Returns a list of error messages (empty if valid).
- **`read_essay()`** — Read essay content from a file.
- **`ConfigManager`** — Loads and provides access to config.yaml settings.
- **`RubricCriterion`** — A single criterion within a rubric.
- **`Rubric`** — A grading rubric consisting of multiple criteria.

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
