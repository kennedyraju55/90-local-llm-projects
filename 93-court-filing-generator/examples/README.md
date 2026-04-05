# Court Filing Generator — Examples

## Overview

This directory contains example scripts demonstrating how to use the Court Filing Generator.

## Files

| File | Description |
|------|-------------|
| `demo.py` | Comprehensive demo showing all core features |

## Running the Demo

```bash
# Make sure Ollama is running
ollama serve &
ollama pull gemma4

# Run the demo
python examples/demo.py
```

## What the Demo Shows

1. **Filing Header Formatting** — How to create a standard court document caption
2. **Template Listing** — All 10 filing templates available
3. **Filing Generation** — Generate a Motion to Dismiss with facts and arguments
4. **Motion Generation** — Generate a Motion to Compel Discovery
5. **Discovery Requests** — Generate interrogatories from a list of topics

## Using the API Programmatically

```python
from src.filing_generator.core import (
    CaseInfo,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
)

# Create case info
case = CaseInfo(
    case_number="2025-CV-00001",
    court="United States District Court",
    parties={"plaintiff": "Jane Doe", "defendant": "Acme Corp"},
    judge="Hon. Judge Smith",
)

# Generate a complaint
result = generate_filing(
    filing_type="complaint",
    case_info=case,
    facts="Describe the facts here...",
    arguments="Legal arguments...",
)

print(result.content)
```

## Privacy Note

🔒 All processing occurs locally using Gemma 4 via Ollama. No data is ever sent to external servers. Attorney-client privilege is preserved.
