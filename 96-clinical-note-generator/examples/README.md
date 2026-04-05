# Clinical Note Generator - Examples

## Quick Demo

```bash
python examples/demo.py
```

## Programmatic Usage

```python
from clinical_note_generator.core import generate_soap_note

# Generate a SOAP note
encounter = "45-year-old female with acute onset headache..."
note = generate_soap_note(encounter, specialty="internal_medicine")
print(note)
```

## Generate Specific Sections

```python
from clinical_note_generator.core import generate_note_section

subjective = generate_note_section("Patient encounter...", section="S")
plan = generate_note_section("Patient encounter...", section="P")
```

## Refine Notes

```python
from clinical_note_generator.core import refine_note

refined = refine_note(original_note, "Add more detail to the Plan section")
```

⚠️ **MEDICAL DISCLAIMER:** All generated notes are AI-assisted drafts and must be reviewed by a qualified physician.
