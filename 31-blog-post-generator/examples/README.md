# Examples for Blog Post Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from a YAML file.
- **`setup_logging()`** — Configure the root logger based on *config*.
- **`build_prompt()`** — Build the blog post generation prompt.
- **`generate_blog_post()`** — Generate a blog post using the LLM.
- **`generate_outline()`** — Generate an outline preview before creating the full post.
- **`BlogPost`** — Represents a generated blog post with metadata.

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
