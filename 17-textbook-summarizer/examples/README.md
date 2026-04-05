# Examples for Textbook Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`read_chapter_file()`** — Read and return the contents of a textbook chapter file.
- **`detect_chapter_info()`** — Attempt to detect chapter number and title from the text.
- **`summarize_chapter()`** — Generate a structured summary of a textbook chapter using the LLM.
- **`summarize_multi_chapter()`** — Summarize all chapters found in a multi-chapter textbook file.
- **`generate_glossary()`** — Generate a key terms glossary from the chapter text.

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
