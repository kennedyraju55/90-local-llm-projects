# Examples for Poem Lyrics Generator

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`build_prompt()`** — Build the poem/lyrics generation prompt.
- **`generate_poem()`** — Generate a poem or lyrics using the LLM.
- **`generate_with_rhyme_scheme()`** — Generate a poem following a specific rhyme scheme (e.g. 'ABAB').
- **`mix_styles()`** — Generate a poem that mixes two poetic styles.
- **`count_syllables()`** — Estimate syllable count per line using a vowel-cluster heuristic.
- **`Poem`** — Represents a single poem or lyric.
- **`PoemCollection`** — A named collection of poems.

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
