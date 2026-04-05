"""Utility helpers for Resume Analyzer."""

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


def read_file(filepath: str) -> str:
    """Read and return contents of a text file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise click.ClickException(f"File not found: {filepath}")
    except PermissionError:
        raise click.ClickException(f"Permission denied: {filepath}")
    except Exception as e:
        raise click.ClickException(f"Error reading {filepath}: {e}")


def parse_json_response(response: str) -> dict:
    """Parse a JSON response from the LLM, handling common formatting issues."""
    cleaned = response.strip()
    cleaned = re.sub(r"^```(?:json)?\s*\n?", "", cleaned)
    cleaned = re.sub(r"\n?```\s*$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", cleaned)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        raise click.ClickException(
            "Failed to parse LLM response as JSON. "
            "Try running again — LLM output can vary between runs."
        )
