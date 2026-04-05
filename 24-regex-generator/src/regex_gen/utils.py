"""Utility helpers for Regex Gen."""

import re
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run_regex_test(pattern: str, test_strings: list[str]) -> list[dict]:
    """Test a regex pattern against a list of strings."""
    results = []
    try:
        compiled = re.compile(pattern)
        for s in test_strings:
            match = compiled.search(s)
            all_matches = compiled.findall(s)
            results.append({
                "string": s,
                "matches": bool(match),
                "match_text": match.group() if match else None,
                "span": match.span() if match else None,
                "all_matches": all_matches,
                "groups": match.groups() if match else (),
            })
    except re.error as e:
        logger.error("Invalid regex pattern '%s': %s", pattern, e)
        return [{"string": s, "matches": False, "error": str(e)} for s in test_strings]
    return results


def validate_regex(pattern: str) -> dict:
    """Validate a regex pattern and return info."""
    try:
        compiled = re.compile(pattern)
        return {
            "valid": True,
            "pattern": pattern,
            "groups": compiled.groups,
            "flags": compiled.flags,
        }
    except re.error as e:
        return {
            "valid": False,
            "pattern": pattern,
            "error": str(e),
        }


def extract_regex_from_text(text: str) -> list[str]:
    """Extract regex patterns from LLM response text (from code blocks)."""
    patterns = []
    code_blocks = re.findall(r'`([^`]+)`', text)
    for block in code_blocks:
        block = block.strip()
        if any(c in block for c in r'[]\.*+?^${}()|') and len(block) > 2:
            try:
                re.compile(block)
                patterns.append(block)
            except re.error:
                pass
    return patterns


def highlight_matches(text: str, pattern: str) -> str:
    """Return text with matches highlighted using markers."""
    try:
        compiled = re.compile(pattern)
        def replacer(m):
            return f">>>{m.group()}<<<"
        return compiled.sub(replacer, text)
    except re.error:
        return text
