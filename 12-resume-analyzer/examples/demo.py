"""
Demo script for Resume Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.resume_analyzer.core import analyze_resume, score_against_jd, simulate_ats_score, compare_resumes, generate_improvement_suggestions


def main():
    """Run a quick demo of Resume Analyzer."""
    print("=" * 60)
    print("🚀 Resume Analyzer - Demo")
    print("=" * 60)
    print()
    # Perform a general analysis of a resume.
    print("📝 Example: analyze_resume()")
    result = analyze_resume(
        resume_text="John Doe\nSoftware Engineer\n5 years experience in Python, Java, and cloud services."
    )
    print(f"   Result: {result}")
    print()
    # Score a resume against a specific job description.
    print("📝 Example: score_against_jd()")
    result = score_against_jd(
        resume_text="John Doe\nSoftware Engineer\n5 years experience in Python, Java, and cloud services.",
        jd_text="Senior Python developer with 5+ years experience in cloud services."
    )
    print(f"   Result: {result}")
    print()
    # Simulate an ATS (Applicant Tracking System) score.
    print("📝 Example: simulate_ats_score()")
    result = simulate_ats_score(
        resume_text="John Doe\nSoftware Engineer\n5 years experience in Python, Java, and cloud services.",
        jd_text="Senior Python developer with 5+ years experience in cloud services."
    )
    print(f"   Result: {result}")
    print()
    # Compare multiple resumes, optionally against a job description.
    print("📝 Example: compare_resumes()")
    result = compare_resumes(
        resume_texts=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
