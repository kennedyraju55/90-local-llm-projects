#!/usr/bin/env python3
"""
Contract Clause Analyzer - Demo Script

Demonstrates the core functionality of the Contract Clause Analyzer.
Requires Ollama to be running with a Gemma 4 model.

🔒 Privacy: All processing happens locally. No data leaves your machine.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from contract_analyzer.core import (
    analyze_clause,
    analyze_contract,
    compare_clauses,
    get_risk_emoji,
    SAMPLE_CLAUSES,
    check_ollama_running,
)


def demo_clause_analysis():
    """Demonstrate single clause analysis."""
    print("=" * 60)
    print("📋 DEMO: Single Clause Analysis")
    print("=" * 60)
    
    clause = SAMPLE_CLAUSES["indemnification"]
    print(f"\nClause:\n{clause}\n")
    
    result = analyze_clause(clause)
    emoji = get_risk_emoji(result.risk_level)
    
    print(f"Type: {result.clause_type}")
    print(f"Risk: {emoji} {result.risk_level.upper()}")
    print(f"Summary: {result.summary}")
    print(f"Obligations: {', '.join(result.obligations)}")
    print(f"Red Flags: {', '.join(result.red_flags)}")
    print(f"Recommendations: {', '.join(result.recommendations)}")


def demo_comparison():
    """Demonstrate clause comparison."""
    print("\n" + "=" * 60)
    print("🔍 DEMO: Clause Comparison")
    print("=" * 60)
    
    clause_a = SAMPLE_CLAUSES["termination"]
    clause_b = SAMPLE_CLAUSES["non_compete"]
    
    result = compare_clauses(clause_a, clause_b)
    
    print(f"\nDifferences: {result.get('differences', [])}")
    print(f"Recommendation: {result.get('recommendation', 'N/A')}")


if __name__ == "__main__":
    if not check_ollama_running():
        print("❌ Ollama is not running. Start it with: ollama serve")
        sys.exit(1)
    
    demo_clause_analysis()
    demo_comparison()
    print("\n✅ Demo complete!")
