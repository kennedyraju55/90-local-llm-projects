# Examples for Debate Topic Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Call load_config
- **`generate_debate_topics()`** — Generate debate topics using the LLM.
- **`generate_moderator_guide()`** — Generate a moderator guide for a debate motion.
- **`rate_evidence_strength()`** — Rate the strength of a piece of evidence.
- **`check_service()`** — Call check_service
- **`Argument`** — Use Argument
- **`CounterargumentPair`** — Use CounterargumentPair
- **`JudgingCriteria`** — Use JudgingCriteria

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
