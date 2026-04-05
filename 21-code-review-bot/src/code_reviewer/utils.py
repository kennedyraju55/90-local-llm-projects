"""Utility helpers for Code Reviewer."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

EXTENSION_MAP = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".java": "java", ".go": "go", ".rs": "rust", ".cpp": "cpp",
    ".c": "c", ".rb": "ruby", ".php": "php", ".sh": "bash",
    ".sql": "sql", ".html": "html", ".css": "css", ".jsx": "jsx",
    ".tsx": "tsx", ".kt": "kotlin", ".swift": "swift", ".scala": "scala",
    ".r": "r", ".m": "matlab", ".cs": "csharp",
}

SEVERITY_COLORS = {
    "HIGH": "red",
    "MEDIUM": "yellow",
    "LOW": "blue",
}

CATEGORY_ICONS = {
    "BUG": "🐛",
    "STYLE": "🎨",
    "SECURITY": "🔒",
    "PERFORMANCE": "⚡",
    "BEST_PRACTICE": "📏",
}


def detect_language(filename: str) -> str:
    """Detect programming language from file extension."""
    _, ext = os.path.splitext(filename)
    return EXTENSION_MAP.get(ext.lower(), "text")


def read_file_safe(filepath: str, max_size_kb: int = 500) -> Optional[str]:
    """Read a file with size limit and error handling."""
    if not os.path.exists(filepath):
        logger.error("File not found: %s", filepath)
        return None

    size_kb = os.path.getsize(filepath) / 1024
    if size_kb > max_size_kb:
        logger.warning("File %s exceeds size limit (%.1f KB > %d KB)", filepath, size_kb, max_size_kb)
        return None

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        logger.error("Error reading file %s: %s", filepath, e)
        return None


def number_lines(code: str) -> str:
    """Add line numbers to code string."""
    return "\n".join(f"{i + 1}: {line}" for i, line in enumerate(code.splitlines()))


def truncate_text(text: str, max_chars: int = 5000) -> str:
    """Truncate text to max_chars with ellipsis indicator."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n... (truncated)"


def calculate_severity_score(issues: list[dict]) -> dict:
    """Calculate an overall severity score from review issues."""
    weights = {"HIGH": 10, "MEDIUM": 5, "LOW": 1}
    total = 0
    counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for issue in issues:
        severity = issue.get("severity", "LOW").upper()
        counts[severity] = counts.get(severity, 0) + 1
        total += weights.get(severity, 0)

    max_score = 100
    score = max(0, max_score - total)
    grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D" if score >= 40 else "F"

    return {"score": score, "grade": grade, "counts": counts, "total_issues": sum(counts.values())}


def format_report_filename(filepath: str, ext: str = "md") -> str:
    """Generate a report filename from the source filepath."""
    base = os.path.splitext(os.path.basename(filepath))[0]
    return f"review_{base}.{ext}"
