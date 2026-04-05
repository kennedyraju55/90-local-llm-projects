"""
Demo script for Deposition Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.deposition_summarizer.core import (
    SAMPLE_TRANSCRIPT,
    summarize_deposition,
    find_admissions,
    find_contradictions,
    extract_testimony,
    generate_follow_up_questions,
    build_timeline,
)


def main():
    """Run a quick demo of Deposition Summarizer."""
    print("=" * 60)
    print("⚖️  Deposition Summarizer — Demo")
    print("=" * 60)
    print()

    print("📝 Example: summarize_deposition()")
    print("   Generates a comprehensive deposition summary...")
    result = summarize_deposition(SAMPLE_TRANSCRIPT)
    print(f"   Witness: {result.witness}")
    print(f"   Title: {result.title}")
    print(f"   Admissions: {len(result.key_admissions)}")
    print(f"   Contradictions: {len(result.contradictions)}")
    print()

    print("📝 Example: find_admissions()")
    print("   Extracts key admissions from the transcript...")
    admissions = find_admissions(SAMPLE_TRANSCRIPT)
    for adm in admissions:
        print(f"   [{adm.significance}] {adm.speaker}: {adm.statement}")
    print()

    print("📝 Example: find_contradictions()")
    print("   Detects contradictions in testimony...")
    contradictions = find_contradictions(SAMPLE_TRANSCRIPT)
    for con in contradictions:
        print(f"   A: {con.statement_a}")
        print(f"   B: {con.statement_b}")
        print(f"   → {con.explanation}")
    print()

    print("📝 Example: extract_testimony(topic='safety valve')")
    print("   Extracts testimony on a specific topic...")
    testimony = extract_testimony(SAMPLE_TRANSCRIPT, "safety valve")
    for t in testimony:
        print(f"   [{t.relevance}] {t.speaker}: {t.summary}")
    print()

    print("📝 Example: generate_follow_up_questions()")
    print("   Suggests follow-up questions...")
    questions = generate_follow_up_questions(SAMPLE_TRANSCRIPT)
    for i, q in enumerate(questions, 1):
        print(f"   {i}. {q}")
    print()

    print("📝 Example: build_timeline()")
    print("   Builds a chronological timeline...")
    timeline = build_timeline(SAMPLE_TRANSCRIPT)
    for event in timeline:
        print(f"   {event['date']}: {event['event']}")
    print()

    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
