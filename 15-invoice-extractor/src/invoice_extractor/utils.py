"""Utility helpers for Invoice Extractor."""

import json
import logging
import os
import re
import sys

import click

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_llm_client():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    from common.llm_client import chat, generate, check_ollama_running
    return chat, generate, check_ollama_running


def read_invoice_file(filepath: str) -> str:
    """Read and return contents of an invoice text file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise click.ClickException(f"File not found: {filepath}")
    except PermissionError:
        raise click.ClickException(f"Permission denied: {filepath}")
    except Exception as exc:
        raise click.ClickException(f"Error reading file: {exc}")


def parse_llm_json(response: str) -> dict:
    """Parse a JSON object from the LLM response, tolerating markdown fences."""
    cleaned = re.sub(r"```(?:json)?\s*", "", response)
    cleaned = cleaned.strip().rstrip("`")

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise click.ClickException(
        "Failed to parse JSON from LLM response. Raw output:\n" + response
    )
