# Examples - Contract Clause Analyzer

## Demo Script

Run the demo to see the analyzer in action:

```bash
# Make sure Ollama is running
ollama serve

# Pull the model
ollama pull gemma4:latest

# Run the demo
python examples/demo.py
```

## Usage Examples

### Analyze a Single Clause
```python
from contract_analyzer.core import analyze_clause

result = analyze_clause("""
    Party A shall indemnify Party B against all claims arising 
    from Party A's breach of this Agreement.
""")

print(f"Risk Level: {result.risk_level}")
print(f"Red Flags: {result.red_flags}")
```

### Analyze a Full Contract
```python
from contract_analyzer.core import analyze_contract

with open("my_contract.txt") as f:
    result = analyze_contract(f.read())

print(f"Overall Risk: {result.overall_risk}")
for clause in result.clause_analyses:
    print(f"  {clause.clause_type}: {clause.risk_level}")
```

### Compare Two Clauses
```python
from contract_analyzer.core import compare_clauses

result = compare_clauses(clause_a_text, clause_b_text)
print(f"Recommendation: {result['recommendation']}")
```

## API Examples

```bash
# Health check
curl http://localhost:8000/health

# Analyze a clause
curl -X POST http://localhost:8000/analyze/clause \
  -H "Content-Type: application/json" \
  -d '{"text": "Party A shall indemnify Party B..."}'

# Get sample clauses
curl http://localhost:8000/samples
```
