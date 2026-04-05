# Examples for Password Strength Advisor

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`calculate_entropy()`** — Calculate password entropy in bits.
- **`check_breach_database()`** — Check if a password is in known breach databases (conceptual local check).
- **`generate_policy()`** — Generate a password policy based on NIST SP 800-63B.
- **`analyze_password_llm()`** — Analyze a password using the LLM (masked characteristics only).
- **`analyze_policy_llm()`** — Analyze a password policy using the LLM.
- **`StrengthLevel`** — Use StrengthLevel
- **`EntropyResult`** — Password entropy calculation result.
- **`BreachCheckResult`** — Breach database check result (conceptual).

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
