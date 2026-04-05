#!/usr/bin/env python3
"""Demo script for Legal Case Researcher.

Demonstrates all core functions with sample legal scenarios.
Requires Ollama running locally with Gemma 4 model.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from common.llm_client import check_ollama_running
from src.case_researcher.core import (
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
    LEGAL_DISCLAIMER,
    SAMPLE_SCENARIOS,
)


def separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def demo_research():
    separator("1. Research Case Law")
    query = "What constitutes a material breach of contract?"
    print(f"Query: {query}\n")
    result = research_case_law(query, jurisdiction="federal")
    print(f"Summary: {result.summary}\n")
    for case in result.relevant_cases:
        print(f"  - {case.case_name} ({case.citation})")
        print(f"    Holding: {case.key_holding}\n")
    if result.key_legal_principles:
        print("Key Principles:")
        for p in result.key_legal_principles:
            print(f"  • {p}")


def demo_precedents():
    separator("2. Find Precedents")
    scenario = SAMPLE_SCENARIOS["employment_discrimination"]
    print(f"Scenario: {scenario['title']}")
    print(f"Facts: {scenario['facts']}\n")
    results = find_precedents(scenario["facts"], scenario["query"])
    for p in results:
        print(f"  - {p.case_name} (Relevance: {p.relevance_score:.0%})")
        print(f"    Recommendation: {p.recommendation}\n")


def demo_analyze():
    separator("3. Analyze Legal Argument")
    argument = (
        "The defendant's actions constitute negligence per se because they violated "
        "a federal safety regulation designed to protect the class of persons to which "
        "the plaintiff belongs, and the harm suffered was the type the regulation was "
        "intended to prevent."
    )
    print(f"Argument: {argument}\n")
    result = analyze_legal_argument(argument)
    print(f"Strength: {result.strength.upper()}")
    print(f"Confidence: {result.confidence_score:.0%}")
    if result.supporting_points:
        print("\nSupporting Points:")
        for sp in result.supporting_points:
            print(f"  ✅ {sp}")
    if result.weaknesses:
        print("\nWeaknesses:")
        for w in result.weaknesses:
            print(f"  ❌ {w}")


def demo_citations():
    separator("4. Extract Citations")
    text = (
        "The court relied on Brown v. Board of Education, 347 U.S. 483 (1954) and "
        "Marbury v. Madison, 5 U.S. 137 (1803) to establish the principle that "
        "constitutional rights cannot be denied through legislative action."
    )
    print(f"Text: {text}\n")
    results = extract_citations(text)
    for c in results:
        print(f"  - {c.case_name} — {c.citation}")


def demo_summarize():
    separator("5. Summarize Case")
    case_text = (
        "Miranda v. Arizona, 384 U.S. 436 (1966). The Supreme Court held that "
        "statements made by a defendant during custodial interrogation are inadmissible "
        "unless the prosecution demonstrates that the defendant was informed of their "
        "right to consult with an attorney and their right against self-incrimination "
        "prior to questioning. Chief Justice Warren delivered the opinion of the Court."
    )
    print(f"Case excerpt: {case_text}\n")
    result = summarize_case(case_text)
    if not result.get("parse_error"):
        print(f"Case: {result.get('case_name', 'N/A')}")
        print(f"Court: {result.get('court', 'N/A')}")
        print(f"Holding: {result.get('holding', 'N/A')}")
        print(f"Significance: {result.get('significance', 'N/A')}")


def main():
    print("⚖️  Legal Case Researcher — Demo")
    print("=" * 60)
    print(f"\n{LEGAL_DISCLAIMER}\n")

    if not check_ollama_running():
        print("❌ Ollama is not running. Start it with: ollama serve")
        print("   Then run this demo again.")
        sys.exit(1)

    print("✅ Ollama is running\n")

    demo_research()
    demo_precedents()
    demo_analyze()
    demo_citations()
    demo_summarize()

    separator("Demo Complete")
    print("🔒 All processing was done locally. No data left this machine.\n")


if __name__ == "__main__":
    main()
