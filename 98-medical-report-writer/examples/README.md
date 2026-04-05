# Examples for Medical Report Writer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml or use defaults.
- **`REPORT_TYPES`** — Browse all available report types (discharge summary, referral letter, etc.).
- **`display_disclaimer()`** — Display the physician review disclaimer.
- **`format_report()`** — Format raw reports in different styles (standard, compact, detailed).
- **`extract_key_findings()`** — Extract key findings and action items from report text.
- **`ReportSession`** — Track generated reports across a session.

## Prerequisites

- Python 3.10+
- Ollama running with Gemma 4 model (for actual report generation)
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
from medical_report_writer.core import generate_report, generate_discharge_summary

# Generate a progress note
report = generate_report(
    clinical_data="Patient presents with productive cough, fever 101.2F...",
    report_type="progress_note",
)

# Generate a discharge summary
summary = generate_discharge_summary(
    admission_data="Admitted 2024-01-15 for community-acquired pneumonia",
    hospital_course="IV antibiotics x 5 days, oxygen therapy...",
    discharge_info="Discharge with oral antibiotics, follow-up in 2 weeks",
)
```
