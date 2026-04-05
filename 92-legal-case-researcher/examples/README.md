# Legal Case Researcher — Usage Examples

## Python API

```python
from src.case_researcher.core import (
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
)

# Research case law
result = research_case_law(
    "What constitutes a material breach of contract?",
    jurisdiction="federal",
)
print(result.summary)
for case in result.relevant_cases:
    print(f"  {case.case_name} — {case.citation}")

# Find precedents
precedents = find_precedents(
    case_facts="Employee was terminated after filing a safety complaint.",
    legal_issue="Wrongful termination / whistleblower retaliation",
)
for p in precedents:
    print(f"  {p.case_name} (Relevance: {p.relevance_score:.0%})")

# Analyze an argument
analysis = analyze_legal_argument(
    "The defendant owed a duty of care to the plaintiff as a business invitee."
)
print(f"Strength: {analysis.strength}")

# Extract citations from text
citations = extract_citations(
    "As held in Roe v. Wade, 410 U.S. 113 (1973), privacy is fundamental."
)

# Summarize a case
summary = summarize_case(open("case_document.txt").read())
print(summary["holding"])
```

## CLI

```bash
# Research case law
case-researcher research "What is the standard for summary judgment?"

# Find precedents
case-researcher precedents --facts "Tenant was evicted without notice" --issue "Due process in evictions"

# Analyze an argument
case-researcher analyze "The statute of limitations has expired, barring the claim."

# Extract citations from a file
case-researcher citations path/to/legal_brief.txt

# Summarize a case
case-researcher summarize path/to/case_opinion.txt

# View sample scenarios
case-researcher samples

# Show disclaimer
case-researcher disclaimer
```

## REST API

```bash
# Start the API server
uvicorn src.case_researcher.api:app --host 0.0.0.0 --port 8000

# Health check
curl http://localhost:8000/health

# Research case law
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"query": "Material breach of contract", "jurisdiction": "federal"}'

# Find precedents
curl -X POST http://localhost:8000/precedents \
  -H "Content-Type: application/json" \
  -d '{"case_facts": "Employee was fired after reporting safety violations", "legal_issue": "Whistleblower retaliation"}'

# Analyze argument
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"argument": "The non-compete clause is unenforceable due to lack of consideration."}'

# Extract citations
curl -X POST http://localhost:8000/citations \
  -H "Content-Type: application/json" \
  -d '{"text": "In Brown v. Board of Education, 347 U.S. 483 (1954)..."}'

# Summarize case
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"case_text": "Full case text goes here..."}'

# Get sample scenarios
curl http://localhost:8000/samples
```

## Web UI

```bash
# Start the Streamlit web interface
streamlit run src/case_researcher/web_ui.py --server.port 8501
```

Then open http://localhost:8501 in your browser.

## Docker

```bash
# Build and run all services
docker-compose up --build

# Web UI: http://localhost:8501
# API:    http://localhost:8000/docs
```
