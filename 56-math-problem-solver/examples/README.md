# Examples for Math Problem Solver

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from YAML file.
- **`get_formula_library()`** — Return formulas from the built-in library, optionally filtered by category.
- **`solve_problem()`** — Solve a math problem using the LLM and return structured result.
- **`generate_practice_problems()`** — Generate practice problems for a given category and difficulty.
- **`get_formulas_from_llm()`** — Fetch an extended formula library from the LLM.
- **`SolutionStep`** — Use SolutionStep
- **`Solution`** — Use Solution
- **`MathProblemResult`** — Use MathProblemResult

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
