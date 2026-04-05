"""Utility helpers for Stack Explainer."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

LANGUAGE_INDICATORS = {
    "python": ["Traceback (most recent call last)", 'File "', '.py"', "SyntaxError", "IndentationError"],
    "javascript": ["at Object.", "at Module.", "node_modules", ".js:", "TypeError:", "ReferenceError:"],
    "java": ["at java.", "at com.", "at org.", ".java:", "Exception in thread", "NullPointerException"],
    "csharp": ["at System.", "at Microsoft.", ".cs:line", "NullReferenceException", "StackTrace:"],
    "go": ["goroutine", "panic:", ".go:", "runtime."],
    "rust": ["thread 'main' panicked", ".rs:", "backtrace:"],
    "ruby": [".rb:", "from (irb)", "NoMethodError", "RuntimeError"],
    "php": ["PHP Fatal error", ".php:", "Stack trace:", "thrown in"],
    "kotlin": [".kt:", "at kotlin.", "KotlinNullPointerException"],
    "swift": [".swift:", "Fatal error:", "Thread 1:"],
}

COMMON_ERRORS = {
    "python": {
        "KeyError": "Accessing a dictionary key that doesn't exist",
        "TypeError": "Operation on incompatible types",
        "ValueError": "Function received an argument of wrong value",
        "AttributeError": "Accessing a non-existent attribute",
        "ImportError": "Module could not be imported",
        "IndexError": "List index out of range",
        "FileNotFoundError": "File or directory not found",
        "ZeroDivisionError": "Division by zero",
    },
    "javascript": {
        "TypeError": "Operation on undefined or null value",
        "ReferenceError": "Variable used before declaration",
        "SyntaxError": "Invalid JavaScript syntax",
        "RangeError": "Number outside of allowed range",
    },
    "java": {
        "NullPointerException": "Accessing a method/field on a null reference",
        "ArrayIndexOutOfBoundsException": "Array index out of bounds",
        "ClassNotFoundException": "Class not found in classpath",
        "StackOverflowError": "Recursive call with no base case",
    },
}


def detect_language(trace: str) -> str:
    """Detect programming language from a stack trace."""
    trace_lower = trace.lower()
    best_lang = "unknown"
    best_matches = 0
    for lang, keywords in LANGUAGE_INDICATORS.items():
        matches = sum(1 for kw in keywords if kw.lower() in trace_lower)
        if matches > best_matches:
            best_matches = matches
            best_lang = lang
    return best_lang if best_matches >= 2 else "unknown"


def read_trace_from_file(filepath: str) -> Optional[str]:
    """Read stack trace from a file."""
    if not os.path.exists(filepath):
        logger.error("File not found: %s", filepath)
        return None
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        logger.error("Error reading file %s: %s", filepath, e)
        return None


def truncate_trace(trace: str, max_chars: int = 5000) -> str:
    """Truncate trace to max_chars."""
    if len(trace) <= max_chars:
        return trace
    return trace[:max_chars] + "\n... (truncated)"


def extract_error_type(trace: str) -> Optional[str]:
    """Try to extract the main error type from a stack trace."""
    lines = trace.strip().splitlines()
    for line in reversed(lines):
        line = line.strip()
        if "Error" in line or "Exception" in line or "panic" in line.lower():
            return line
    return None


def get_error_hint(language: str, error_type: str) -> Optional[str]:
    """Look up a common error hint from the solution database."""
    errors = COMMON_ERRORS.get(language, {})
    for key, desc in errors.items():
        if key in error_type:
            return desc
    return None
