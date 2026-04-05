# Examples — Legal Brief Writer

## Quick Start

### Run the Demo
```bash
cd 95-legal-brief-writer
python examples/demo.py
```

### Prerequisites
1. Install [Ollama](https://ollama.ai)
2. Pull Gemma 4: `ollama pull gemma4:latest`
3. Install dependencies: `pip install -r requirements.txt`

## Usage Examples

### Write a Brief (CLI)
```bash
brief-writer write \
  --type memorandum_of_law \
  --case-name "Smith v. Jones" \
  --facts-file facts.txt \
  --issues "Whether defendant breached duty of care" \
  --arguments "Defendant failed to maintain premises" \
  --output brief.txt
```

### Write a Memorandum (CLI)
```bash
brief-writer memo \
  --case-name "Doe v. Roe" \
  --question "Is the employer vicariously liable?" \
  --facts "Employee caused accident during work hours" \
  --output memo.txt
```

### IRAC Analysis (CLI)
```bash
brief-writer irac \
  --issue "Whether a duty of care exists" \
  --facts "Plaintiff was injured on defendant's property"
```

### Improve Writing (CLI)
```bash
brief-writer improve \
  --text "The defendant was careless and hurt the plaintiff"
```

### Python API
```python
from src.brief_writer.core import (
    CaseDetails, write_brief, write_memorandum,
    write_irac_analysis, improve_legal_writing
)

# Write a brief
case = CaseDetails(case_name="Smith v. Jones", court="District Court")
result = write_brief(
    brief_type="trial_brief",
    case_details=case,
    facts="The plaintiff alleges...",
    issues="Negligence",
    arguments="Defendant breached duty",
)
print(result.title)
for section in result.sections:
    print(f"{section.title}: {section.content[:100]}...")
```

### REST API
```bash
# Start the API server
uvicorn src.brief_writer.api:app --host 0.0.0.0 --port 8000

# Generate a brief
curl -X POST http://localhost:8000/brief \
  -H "Content-Type: application/json" \
  -d '{
    "brief_type": "memorandum_of_law",
    "case_details": {"case_name": "Smith v. Jones"},
    "facts": "The plaintiff alleges...",
    "issues": "Negligence",
    "arguments": "Defendant breached duty"
  }'
```

## Supported Brief Types

| Type | Description |
|------|-------------|
| `trial_brief` | Brief filed with trial court |
| `appellate_brief` | Brief for appellate court |
| `amicus_brief` | Friend of the court brief |
| `memorandum_of_law` | Legal arguments on a motion |
| `memorandum_in_support` | Supporting a motion |
| `memorandum_in_opposition` | Opposing a motion |
| `reply_brief` | Reply to opposition |
| `legal_memorandum` | Internal objective memo |
| `case_summary` | Concise case summary |
