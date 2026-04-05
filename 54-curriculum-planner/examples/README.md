# Examples for Curriculum Planner

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`setup_logging()`** — Configure the root logger from config.
- **`parse_response()`** — Parse a JSON response from the LLM, stripping markdown fences.
- **`generate_curriculum()`** — Generate a curriculum using the LLM (enhanced from app.py).
- **`validate_curriculum_data()`** — Validate curriculum data and return a list of issues (empty = valid).
- **`build_course_design()`** — Convert raw LLM JSON dict into a CourseDesign dataclass.
- **`ConfigManager`** — Loads and provides access to config.yaml settings.
- **`LearningOutcome`** — Use LearningOutcome
- **`WeekPlan`** — Use WeekPlan

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
