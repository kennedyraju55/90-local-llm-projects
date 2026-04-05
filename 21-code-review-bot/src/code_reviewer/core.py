"""Core business logic for Code Reviewer."""

import os
import sys
import json
import logging
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import ReviewConfig, load_config
from .utils import (
    detect_language, read_file_safe, number_lines, truncate_text,
    calculate_severity_score, CATEGORY_ICONS,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an expert code reviewer. Analyze the provided code and give detailed feedback.
For each issue found, provide:
1. Line number(s) affected
2. Category: BUG, STYLE, SECURITY, PERFORMANCE, or BEST_PRACTICE
3. Severity: HIGH, MEDIUM, or LOW
4. Description of the issue
5. Suggested fix with code example

Format your response as a structured review with clear sections.
Use markdown formatting for readability.
At the end, provide an overall code quality summary."""

AUTOFIX_PROMPT = """You are an expert programmer. Given the code and the identified issues,
generate corrected code that fixes all HIGH and MEDIUM severity issues.
Preserve the original code structure and style. Add comments where fixes were applied.
Return only the corrected code in a code block."""


def review_single_file(
    filepath: str,
    focus_areas: Optional[list[str]] = None,
    config: Optional[ReviewConfig] = None,
) -> dict:
    """Review a single code file and return structured results."""
    config = config or load_config()
    focus_areas = focus_areas or []

    code = read_file_safe(filepath, max_size_kb=config.max_file_size_kb)
    if code is None:
        return {"filepath": filepath, "error": "Could not read file", "issues": []}

    if not code.strip():
        return {"filepath": filepath, "error": "File is empty", "issues": []}

    filename = os.path.basename(filepath)
    language = detect_language(filename)
    numbered = number_lines(code)

    focus_text = ""
    if focus_areas:
        focus_text = f"\n\nFocus especially on these areas: {', '.join(focus_areas)}"

    prompt = f"""Review the following {language} code file: {filename}{focus_text}

```{language}
{truncate_text(numbered, config.max_tokens * 2)}
```

Provide a thorough code review with specific line references, severity ratings, and fix suggestions."""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Reviewing file: %s (%s)", filepath, language)

    response = chat(
        messages,
        system_prompt=SYSTEM_PROMPT,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return {
        "filepath": filepath,
        "filename": filename,
        "language": language,
        "review": response,
        "code": code,
        "lines": len(code.splitlines()),
    }


def review_multiple_files(
    filepaths: list[str],
    focus_areas: Optional[list[str]] = None,
    config: Optional[ReviewConfig] = None,
) -> list[dict]:
    """Review multiple files and return aggregated results."""
    config = config or load_config()
    results = []
    for fp in filepaths:
        result = review_single_file(fp, focus_areas, config)
        results.append(result)
        logger.info("Completed review for: %s", fp)
    return results


def generate_autofix(filepath: str, review_text: str, config: Optional[ReviewConfig] = None) -> str:
    """Generate auto-fix suggestions based on review results."""
    config = config or load_config()
    code = read_file_safe(filepath)
    if not code:
        return "Could not read file for auto-fix."

    prompt = f"""Original code:
```
{truncate_text(code)}
```

Review findings:
{truncate_text(review_text, 3000)}

Generate the corrected version of the code fixing all HIGH and MEDIUM severity issues."""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages,
        system_prompt=AUTOFIX_PROMPT,
        model=config.model,
        temperature=0.2,
        max_tokens=config.max_tokens,
    )
    return response


def export_report(results: list[dict], output_path: str, fmt: str = "markdown") -> str:
    """Export review results to a file."""
    if fmt == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, default=str)
    else:
        lines = ["# Code Review Report\n"]
        for r in results:
            lines.append(f"## {r.get('filename', 'Unknown')}\n")
            lines.append(f"- **Language:** {r.get('language', 'unknown')}")
            lines.append(f"- **Lines:** {r.get('lines', 0)}\n")
            lines.append(r.get("review", "No review available."))
            lines.append("\n---\n")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    logger.info("Report exported to: %s", output_path)
    return output_path
