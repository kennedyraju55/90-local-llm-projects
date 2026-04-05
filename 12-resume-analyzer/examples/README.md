# Examples for Resume Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`analyze_resume()`** — Perform a general analysis of a resume.
- **`score_against_jd()`** — Score a resume against a specific job description.
- **`simulate_ats_score()`** — Simulate an ATS (Applicant Tracking System) score.
- **`compare_resumes()`** — Compare multiple resumes, optionally against a job description.
- **`generate_improvement_suggestions()`** — Generate detailed improvement suggestions for a resume.

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
