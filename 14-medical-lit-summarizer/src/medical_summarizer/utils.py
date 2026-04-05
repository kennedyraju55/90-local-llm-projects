"""Utility helpers for Medical Literature Summarizer."""

import logging
import os
import sys

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


def read_paper(file_path: str) -> str:
    """Read a paper from a text file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Paper file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise ValueError("Paper file is empty.")

    return content
