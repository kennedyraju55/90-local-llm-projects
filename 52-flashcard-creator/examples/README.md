# Examples for Flashcard Creator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`setup_logging()`** — Configure module-level logging based on config.
- **`parse_response()`** — Strip markdown fences and parse JSON from LLM output.
- **`create_flashcards()`** — Generate flashcards using the LLM.
- **`dict_to_flashcards()`** — Convert raw LLM JSON into a list of Flashcard dataclass instances.
- **`export_deck_json()`** — Export a deck to JSON file. Returns the filepath.
- **`ConfigManager`** — Loads and provides access to config.yaml settings.
- **`Flashcard`** — A single flashcard with spaced-repetition metadata.
- **`Deck`** — A named collection of flashcards.

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
