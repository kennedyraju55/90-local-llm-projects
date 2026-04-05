"""Core business logic for Stack Explainer."""

import os
import sys
import logging
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import ExplainerConfig, load_config
from .utils import detect_language, truncate_trace, extract_error_type, get_error_hint

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an expert software debugger. When given a stack trace or error message:

1. **Error Summary**: Explain the error in plain English (1-2 sentences)
2. **Root Cause**: Identify the most likely root cause
3. **Call Chain**: Walk through the stack trace from bottom to top, explaining each frame
4. **Fix Suggestions**: Provide 2-3 concrete fixes with code examples
5. **Prevention Tips**: How to prevent this error in the future

Be specific, reference line numbers and file names from the trace.
Use markdown formatting."""

FIX_CODE_PROMPT = """You are an expert programmer and debugger. Given a stack trace and error explanation,
generate the corrected code that would fix the error.
Provide the fix as a code block with comments explaining the changes.
If the root cause is unclear, provide the most likely fix based on the error type."""

SIMILAR_ERRORS_PROMPT = """You are an expert debugger. Given a stack trace, identify:
1. The exact error type and its common causes
2. 3-5 similar errors that developers often confuse with this one
3. How to distinguish between them
4. Links to relevant documentation or Stack Overflow patterns

Format with markdown."""


def explain_trace(
    trace: str,
    language: str = "",
    config: Optional[ExplainerConfig] = None,
) -> dict:
    """Analyze a stack trace and return explanation."""
    config = config or load_config()

    detected_lang = language or detect_language(trace)
    error_type = extract_error_type(trace)
    error_hint = get_error_hint(detected_lang, error_type) if error_type and detected_lang != "unknown" else None

    lang_hint = f"\nThis appears to be a {detected_lang} stack trace." if detected_lang != "unknown" else ""
    hint_text = f"\nQuick hint: {error_hint}" if error_hint else ""

    truncated = truncate_trace(trace, config.max_trace_chars)

    prompt = f"""Explain the following stack trace/error in plain English and suggest fixes:{lang_hint}{hint_text}

```
{truncated}
```"""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Explaining trace (language=%s, error=%s)", detected_lang, error_type or "unknown")

    response = chat(
        messages,
        system_prompt=SYSTEM_PROMPT,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return {
        "explanation": response,
        "language": detected_lang,
        "error_type": error_type,
        "error_hint": error_hint,
        "trace_preview": trace.strip()[:2000],
    }


def generate_fix_code(
    trace: str,
    explanation: str,
    config: Optional[ExplainerConfig] = None,
) -> str:
    """Generate fix code based on trace and explanation."""
    config = config or load_config()

    prompt = f"""Stack trace:
```
{truncate_trace(trace, 3000)}
```

Explanation: {explanation[:2000]}

Generate the corrected code that fixes this error."""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages,
        system_prompt=FIX_CODE_PROMPT,
        model=config.model,
        temperature=0.2,
        max_tokens=config.max_tokens,
    )
    return response


def find_similar_errors(
    trace: str,
    config: Optional[ExplainerConfig] = None,
) -> str:
    """Find similar errors and distinguish between them."""
    config = config or load_config()

    prompt = f"""Analyze this error and find similar/related errors:

```
{truncate_trace(trace, 3000)}
```"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages,
        system_prompt=SIMILAR_ERRORS_PROMPT,
        model=config.model,
        temperature=0.3,
        max_tokens=config.max_tokens,
    )
    return response
