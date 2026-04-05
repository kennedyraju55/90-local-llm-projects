"""Core business logic for API Doc Gen."""

import os
import sys
import json
import logging
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import DocGenConfig, load_config
from .utils import (
    find_python_files, extract_functions, format_extracted_info,
    generate_openapi_skeleton,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a technical writer specializing in API documentation.
Given Python source code with extracted function/class signatures, generate professional API documentation in Markdown.

For each function/class, document:
1. Description (inferred from name, docstring, and code)
2. Parameters with types and descriptions
3. Return type and description
4. Example usage
5. Any exceptions that may be raised

Use clean markdown formatting with proper headings, tables, and code blocks."""

OPENAPI_PROMPT = """You are an API documentation expert. Given the extracted API structure,
generate a complete OpenAPI 3.0 specification in YAML format.
Include realistic example request/response bodies, proper schemas, and endpoint grouping.
Use proper OpenAPI 3.0 syntax."""


def generate_docs(
    source_path: str,
    config: Optional[DocGenConfig] = None,
) -> dict:
    """Generate API documentation for all files in the source path."""
    config = config or load_config()
    files = find_python_files(source_path)

    if not files:
        return {"docs": "# API Documentation\n\nNo Python files found.", "files": [], "items_count": 0}

    all_info = []
    all_items = []
    for filepath in files:
        items = extract_functions(filepath)
        if items:
            info = format_extracted_info(filepath, items)
            all_info.append(info)
            all_items.extend(items)
            logger.info("Extracted %d items from %s", len(items), filepath)

    if not all_info:
        return {
            "docs": "# API Documentation\n\nNo functions or classes found.",
            "files": files,
            "items_count": 0,
        }

    combined = "\n\n".join(all_info)
    prompt = f"""Generate comprehensive API documentation in Markdown for the following Python code structure:

{combined[:6000]}

Create a professional API reference document with examples."""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating docs for %d files, %d items", len(files), len(all_items))

    response = chat(
        messages,
        system_prompt=SYSTEM_PROMPT,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return {
        "docs": response,
        "files": files,
        "items_count": len(all_items),
        "all_items": all_items,
    }


def generate_openapi(
    source_path: str,
    config: Optional[DocGenConfig] = None,
) -> dict:
    """Generate OpenAPI specification from source code."""
    config = config or load_config()
    files = find_python_files(source_path)

    all_items = []
    for filepath in files:
        items = extract_functions(filepath)
        all_items.extend(items)

    skeleton = generate_openapi_skeleton(all_items, title=os.path.basename(source_path))

    # Enhance with LLM
    prompt = f"""Enhance this OpenAPI skeleton with better descriptions, examples, and schemas:

```json
{json.dumps(skeleton, indent=2)[:4000]}
```

Return a complete OpenAPI 3.0 spec in YAML format."""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages,
        system_prompt=OPENAPI_PROMPT,
        model=config.model,
        temperature=0.2,
        max_tokens=config.max_tokens,
    )

    return {"openapi_yaml": response, "skeleton": skeleton}


def export_docs(content: str, output_path: str, fmt: str = "markdown") -> str:
    """Export documentation to file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    logger.info("Documentation exported to: %s", output_path)
    return output_path
