# Examples for Deposition Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`summarize_deposition()`** — Generate a comprehensive deposition summary with all analysis fields.
- **`find_admissions()`** — Extract key admissions from the transcript.
- **`find_contradictions()`** — Detect contradictions in witness testimony.
- **`extract_testimony()`** — Extract testimony on a specific topic.
- **`generate_follow_up_questions()`** — Generate suggested follow-up questions for attorneys.
- **`build_timeline()`** — Build a chronological timeline of events mentioned in the deposition.

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

## Programmatic Usage

```python
from src.deposition_summarizer.core import summarize_deposition, find_admissions

# Full summary
summary = summarize_deposition(transcript_text)
print(summary.witness, summary.overall_summary)

# Key admissions only
admissions = find_admissions(transcript_text)
for adm in admissions:
    print(f"[{adm.significance}] {adm.statement}")

# Testimony on a topic
from src.deposition_summarizer.core import extract_testimony
testimony = extract_testimony(transcript_text, "contract terms")
```
