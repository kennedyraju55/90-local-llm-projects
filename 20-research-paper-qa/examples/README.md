# Examples for Research Paper Qa

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_paper()`** — Load and return the contents of a research paper text file.
- **`load_multiple_papers()`** — Load multiple research papers.
- **`build_system_prompt()`** — Build the system prompt with the paper content embedded.
- **`build_multi_paper_content()`** — Build combined content from multiple papers.
- **`ask_question()`** — Send a question to the LLM with full conversation context.

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
