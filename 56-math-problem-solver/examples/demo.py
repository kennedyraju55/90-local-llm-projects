"""
Demo script for Math Problem Solver
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.math_solver.core import load_config, get_formula_library, solve_problem, generate_practice_problems, get_formulas_from_llm, check_service, to_dict, SolutionStep, Solution, MathProblemResult


def main():
    """Run a quick demo of Math Problem Solver."""
    print("=" * 60)
    print("🚀 Math Problem Solver - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Return formulas from the built-in library, optionally filtered by category.
    print("📝 Example: get_formula_library()")
    result = get_formula_library()
    print(f"   Result: {result}")
    print()
    # Solve a math problem using the LLM and return structured result.
    print("📝 Example: solve_problem()")
    result = solve_problem(
        problem="Solve for x: 2x + 5 = 15"
    )
    print(f"   Result: {result}")
    print()
    # Generate practice problems for a given category and difficulty.
    print("📝 Example: generate_practice_problems()")
    result = generate_practice_problems(
        category="general knowledge",
        difficulty="medium"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
