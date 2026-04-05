"""
Demo script for Meeting Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.meeting_summarizer.core import summarize_meeting, identify_speakers, extract_decision_log, generate_followup_reminders, save_summary


def main():
    """Run a quick demo of Meeting Summarizer."""
    print("=" * 60)
    print("🚀 Meeting Summarizer - Demo")
    print("=" * 60)
    print()
    # Send the transcript to the LLM for analysis and summarization.
    print("📝 Example: summarize_meeting()")
    result = summarize_meeting(
        transcript="Alice: Let's discuss Q4.\nBob: Focus on performance.\nAlice: Agreed."
    )
    print(f"   Result: {result}")
    print()
    # Identify and profile speakers from the transcript.
    print("📝 Example: identify_speakers()")
    result = identify_speakers(
        transcript="Alice: Let's discuss Q4.\nBob: Focus on performance.\nAlice: Agreed."
    )
    print(f"   Result: {result}")
    print()
    # Extract a detailed decision log from the transcript.
    print("📝 Example: extract_decision_log()")
    result = extract_decision_log(
        transcript="Alice: Let's discuss Q4.\nBob: Focus on performance.\nAlice: Agreed."
    )
    print(f"   Result: {result}")
    print()
    # Generate follow-up reminders with priorities and deadlines.
    print("📝 Example: generate_followup_reminders()")
    result = generate_followup_reminders(
        transcript="Alice: Let's discuss Q4.\nBob: Focus on performance.\nAlice: Agreed."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
