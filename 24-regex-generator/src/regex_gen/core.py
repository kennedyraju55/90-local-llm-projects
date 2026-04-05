"""Core business logic for Regex Gen."""

import os
import sys
import re
import logging
from typing import Any, Dict, List, Optional, Tuple, Union

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import RegexConfig, load_config, PATTERN_LIBRARY
from .utils import run_regex_test, validate_regex, extract_regex_from_text

logger = logging.getLogger(__name__)

GENERATE_PROMPT = """You are a regex expert. Given a natural language description, generate the best regular expression.

Provide:
1. The regex pattern (in a code block)
2. Explanation of each component
3. Example matches and non-matches
4. Any common edge cases to consider
5. The regex in multiple flavors if relevant (Python, JavaScript, PCRE)

Format with markdown. Put the regex pattern in a code block."""

EXPLAIN_PROMPT = """You are a regex expert. Given a regular expression, explain it in plain English.

Provide:
1. Overall description of what it matches
2. Component-by-component breakdown
3. Example strings that would match
4. Example strings that would NOT match
5. Any potential issues or improvements

Format with markdown."""


def generate_regex(
    description: str,
    flavor: str = "python",
    config: Optional[RegexConfig] = None,
) -> dict:
    """Generate a regex pattern from natural language description."""
    config = config or load_config()

    prompt = f"Generate a regular expression ({flavor} flavor) that matches: {description}"
    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating regex for: %s (flavor=%s)", description, flavor)

    response = chat(
        messages,
        system_prompt=GENERATE_PROMPT,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    patterns = extract_regex_from_text(response)

    return {
        "description": description,
        "explanation": response,
        "extracted_patterns": patterns,
        "primary_pattern": patterns[0] if patterns else None,
        "flavor": flavor,
    }


def explain_regex(
    pattern: str,
    config: Optional[RegexConfig] = None,
) -> dict:
    """Explain an existing regex pattern in plain English."""
    config = config or load_config()

    validation = validate_regex(pattern)
    if not validation["valid"]:
        logger.warning("Pattern may be invalid: %s", validation.get("error"))

    prompt = f"Explain this regular expression in detail:\n\n`{pattern}`"
    messages = [{"role": "user", "content": prompt}]

    response = chat(
        messages,
        system_prompt=EXPLAIN_PROMPT,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return {
        "pattern": pattern,
        "explanation": response,
        "validation": validation,
    }


def get_pattern_from_library(name: str) -> Optional[str]:
    """Look up a pattern from the built-in pattern library."""
    return PATTERN_LIBRARY.get(name.lower())


def list_library_patterns() -> dict:
    """Return the full pattern library."""
    return PATTERN_LIBRARY.copy()
