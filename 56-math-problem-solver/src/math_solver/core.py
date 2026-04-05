"""Core business logic for Math Problem Solver."""

import json
import logging
import os
import sys
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


def load_config(path: str = _CONFIG_PATH) -> dict:
    """Load configuration from YAML file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        logger.warning("Config file not found at %s, using defaults.", path)
        return {}


CONFIG = load_config()

# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class SolutionStep:
    step_number: int
    description: str
    work: str = ""
    explanation: str = ""


@dataclass
class Solution:
    answer: str
    steps: List[SolutionStep] = field(default_factory=list)


@dataclass
class MathProblemResult:
    problem: str = ""
    category: str = ""
    difficulty: str = ""
    solution: Optional[Solution] = None
    concepts_used: List[str] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)
    related_problems: List[str] = field(default_factory=list)
    latex_output: str = ""

    def to_dict(self) -> dict:
        """To dict."""
        return asdict(self)


# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an expert mathematics tutor who solves problems step-by-step.
Return your solution in valid JSON format:

{
  "problem": "The original problem",
  "category": "algebra|calculus|geometry|statistics|arithmetic|trigonometry",
  "difficulty": "basic|intermediate|advanced",
  "solution": {
    "answer": "The final answer",
    "steps": [
      {
        "step_number": 1,
        "description": "What we're doing in this step",
        "work": "The mathematical work shown",
        "explanation": "Why we do this"
      }
    ]
  },
  "concepts_used": ["Concept 1", "Concept 2"],
  "tips": ["Helpful tip for similar problems"],
  "related_problems": ["A similar problem to practice"],
  "latex_output": "LaTeX representation of the solution"
}

Return ONLY the JSON, no other text."""

FORMULA_LIBRARY_PROMPT = """You are a mathematics reference assistant. Return a JSON object with common formulas for the requested category:

{
  "category": "Category name",
  "formulas": [
    {
      "name": "Formula name",
      "formula": "The formula in plain text",
      "latex": "LaTeX representation",
      "description": "When to use this formula",
      "example": "A quick usage example"
    }
  ]
}

Return ONLY the JSON, no other text."""

PRACTICE_PROMPT = """You are a math practice problem generator. Generate practice problems at the specified difficulty.
Return in valid JSON format:

{
  "category": "Category name",
  "difficulty": "Difficulty level",
  "problems": [
    {
      "number": 1,
      "problem": "Problem statement",
      "hint": "A helpful hint",
      "answer": "The correct answer"
    }
  ]
}

Return ONLY the JSON, no other text."""

# ---------------------------------------------------------------------------
# Formula library
# ---------------------------------------------------------------------------

BUILTIN_FORMULAS = {
    "algebra": [
        {"name": "Quadratic Formula", "formula": "x = (-b ± √(b²-4ac)) / 2a", "latex": "x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}", "description": "Solve ax²+bx+c=0"},
        {"name": "Slope-Intercept", "formula": "y = mx + b", "latex": "y = mx + b", "description": "Linear equation form"},
        {"name": "Point-Slope Form", "formula": "y - y₁ = m(x - x₁)", "latex": "y - y_1 = m(x - x_1)", "description": "Line through a point with slope"},
    ],
    "geometry": [
        {"name": "Circle Area", "formula": "A = πr²", "latex": "A = \\pi r^2", "description": "Area of a circle"},
        {"name": "Pythagorean Theorem", "formula": "a² + b² = c²", "latex": "a^2 + b^2 = c^2", "description": "Right triangle sides"},
        {"name": "Triangle Area", "formula": "A = ½bh", "latex": "A = \\frac{1}{2}bh", "description": "Area of a triangle"},
    ],
    "calculus": [
        {"name": "Power Rule", "formula": "d/dx[xⁿ] = nxⁿ⁻¹", "latex": "\\frac{d}{dx}x^n = nx^{n-1}", "description": "Derivative of power function"},
        {"name": "Chain Rule", "formula": "d/dx[f(g(x))] = f'(g(x))·g'(x)", "latex": "\\frac{d}{dx}f(g(x)) = f'(g(x)) \\cdot g'(x)", "description": "Composite function derivative"},
    ],
    "trigonometry": [
        {"name": "sin²+cos²", "formula": "sin²θ + cos²θ = 1", "latex": "\\sin^2\\theta + \\cos^2\\theta = 1", "description": "Fundamental identity"},
        {"name": "Law of Cosines", "formula": "c² = a² + b² - 2ab·cos(C)", "latex": "c^2 = a^2 + b^2 - 2ab\\cos C", "description": "Relate triangle sides and angles"},
    ],
}


def get_formula_library(category: str = "") -> dict:
    """Return formulas from the built-in library, optionally filtered by category."""
    if category and category in BUILTIN_FORMULAS:
        return {"category": category, "formulas": BUILTIN_FORMULAS[category]}
    return {"categories": BUILTIN_FORMULAS}


# ---------------------------------------------------------------------------
# LLM interaction helpers
# ---------------------------------------------------------------------------


def _get_llm_client() -> Tuple[Any, ...]:
    """Import and return the LLM client lazily."""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    from common.llm_client import chat, check_ollama_running
    return chat, check_ollama_running


def _parse_json_response(text: str) -> dict:
    """Parse JSON from an LLM response, stripping markdown fences."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


def _result_from_dict(data: dict) -> MathProblemResult:
    """Convert a raw dict to a MathProblemResult."""
    sol_data = data.get("solution", {})
    steps = [SolutionStep(**s) for s in sol_data.get("steps", [])]
    solution = Solution(answer=sol_data.get("answer", ""), steps=steps)
    return MathProblemResult(
        problem=data.get("problem", ""),
        category=data.get("category", ""),
        difficulty=data.get("difficulty", ""),
        solution=solution,
        concepts_used=data.get("concepts_used", []),
        tips=data.get("tips", []),
        related_problems=data.get("related_problems", []),
        latex_output=data.get("latex_output", ""),
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def solve_problem(problem: str, show_steps: bool = True, category: str = "") -> MathProblemResult:
    """Solve a math problem using the LLM and return structured result."""
    chat, _ = _get_llm_client()

    prompt = f"Solve this math problem with {'detailed step-by-step explanations' if show_steps else 'the answer'}:\n\n{problem}"
    if category:
        prompt += f"\n\nThis is a {category} problem."
    prompt += "\nAlso provide the LaTeX representation of the solution."

    logger.info("Solving problem: %s", problem)

    response = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=float(CONFIG.get("llm", {}).get("temperature", 0.2)),
        max_tokens=int(CONFIG.get("llm", {}).get("max_tokens", 4096)),
    )

    data = _parse_json_response(response)
    logger.info("Problem solved successfully: category=%s", data.get("category"))
    return _result_from_dict(data)


def generate_practice_problems(category: str, difficulty: str, count: int = 5) -> dict:
    """Generate practice problems for a given category and difficulty."""
    chat, _ = _get_llm_client()

    prompt = (
        f"Generate exactly {count} {difficulty} practice problems in the category: {category}.\n"
        f"Include hints and answers."
    )

    logger.info("Generating %d %s %s practice problems", count, difficulty, category)

    response = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=PRACTICE_PROMPT,
        temperature=float(CONFIG.get("llm", {}).get("temperature", 0.5)),
        max_tokens=int(CONFIG.get("llm", {}).get("max_tokens", 4096)),
    )

    return _parse_json_response(response)


def get_formulas_from_llm(category: str) -> dict:
    """Fetch an extended formula library from the LLM."""
    chat, _ = _get_llm_client()

    prompt = f"Provide a comprehensive formula reference for: {category}"
    logger.info("Fetching formula library for: %s", category)

    response = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=FORMULA_LIBRARY_PROMPT,
        temperature=0.2,
        max_tokens=4096,
    )

    return _parse_json_response(response)


def check_service() -> bool:
    """Check if the Ollama service is running."""
    _, check_ollama_running = _get_llm_client()
    return check_ollama_running()
