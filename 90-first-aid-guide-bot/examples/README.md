# Examples for First Aid Guide Bot

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`show_disclaimer()`** — Display the emergency disclaimer prominently.
- **`get_severity_style()`** — Return a rich style string based on severity level.
- **`evaluate_emergency()`** — Evaluate an emergency situation using the decision tree.
- **`get_supply_checklist()`** — Return the first aid supply checklist, optionally filtered by priority.
- **`get_cpr_steps()`** — Return the CPR steps with timing information.
- **`EmergencyContact`** — A single emergency contact.
- **`EmergencyContactManager`** — Manage a list of emergency contacts (in-memory storage).

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
