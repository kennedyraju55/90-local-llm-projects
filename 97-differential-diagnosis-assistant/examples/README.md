# Examples for Differential Diagnosis Assistant

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`load_config()`** — Load configuration from config.yaml or use defaults.
- **`assess_urgency()`** — Assess urgency level based on symptom keywords.
- **`get_affected_systems()`** — Identify which body systems are affected by symptoms.
- **`display_disclaimer()`** — Display the medical disclaimer using rich formatting.
- **`generate_differential()`** — Generate ranked differential diagnoses using the LLM.
- **`get_workup_recommendations()`** — Get recommended workup for a diagnosis.
- **`compare_diagnoses()`** — Compare two diagnoses side by side.
- **`DiagnosisSession`** — Track diagnostic reasoning across a session.

## Programmatic Usage

```python
from differential_diagnosis.core import (
    generate_differential,
    get_workup_recommendations,
    compare_diagnoses,
    assess_urgency,
    DiagnosisSession,
)

# Generate differential diagnosis
result = generate_differential(
    symptoms="sudden onset severe headache, worst of life",
    patient_info="35F, no significant PMH",
    exam_findings="neck stiffness, photophobia",
)
print(result)

# Get workup recommendations
workup = get_workup_recommendations("Subarachnoid hemorrhage")
print(workup)

# Compare two diagnoses
comparison = compare_diagnoses(
    "Subarachnoid hemorrhage",
    "Meningitis",
    "sudden severe headache with neck stiffness",
)
print(comparison)

# Track session
session = DiagnosisSession()
session.add_entry("headache", "35F", "stiff neck", 4, ["neurological"], result)
print(session.get_summary())
```

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
