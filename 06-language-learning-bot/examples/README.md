# Examples for Language Learning Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`get_system_prompt()`** — Build the system prompt for the specified language and level.
- **`get_response()`** — Get a response from the language tutor.
- **`get_lesson()`** — Get a mini lesson on a specific topic.
- **`get_pronunciation_tips()`** — Get pronunciation tips for a word in the target language.
- **`generate_lesson_plan()`** — Generate a structured lesson plan.

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
