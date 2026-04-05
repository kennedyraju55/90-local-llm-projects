# Examples for Social Media Writer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml, with caching.
- **`setup_logging()`** — Configure logging from the loaded config.
- **`build_prompt()`** — Build the social media post generation prompt.
- **`generate_posts()`** — Generate social media posts using the LLM.
- **`validate_char_count()`** — Check whether *content* fits within the platform's character limit.
- **`SocialPost`** — Represents a single social media post with metadata.

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
