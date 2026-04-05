"""
Demo script for Research Paper Qa
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.research_qa.core import load_paper, load_multiple_papers, build_system_prompt, build_multi_paper_content, ask_question, suggest_followup_questions, extract_citations


def main():
    """Run a quick demo of Research Paper Qa."""
    print("=" * 60)
    print("🚀 Research Paper Qa - Demo")
    print("=" * 60)
    print()
    # Load and return the contents of a research paper text file.
    print("📝 Example: load_paper()")
    result = load_paper(
        paper_path="."
    )
    print(f"   Result: {result}")
    print()
    # Load multiple research papers.
    print("📝 Example: load_multiple_papers()")
    result = load_multiple_papers(
        paper_paths=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    # Build the system prompt with the paper content embedded.
    print("📝 Example: build_system_prompt()")
    result = build_system_prompt(
        paper_content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    # Build combined content from multiple papers.
    print("📝 Example: build_multi_paper_content()")
    result = build_multi_paper_content(
        papers={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
