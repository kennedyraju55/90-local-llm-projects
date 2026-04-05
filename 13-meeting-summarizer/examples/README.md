# Examples for Meeting Summarizer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`summarize_meeting()`** — Send the transcript to the LLM for analysis and summarization.
- **`identify_speakers()`** — Identify and profile speakers from the transcript.
- **`extract_decision_log()`** — Extract a detailed decision log from the transcript.
- **`generate_followup_reminders()`** — Generate follow-up reminders with priorities and deadlines.
- **`save_summary()`** — Save the meeting summary to a file.

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
