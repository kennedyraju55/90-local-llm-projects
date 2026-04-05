"""Utility helpers for Legal Document Summarizer."""

import logging
import os
import re
import sys
from typing import Any

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the application."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_llm_client():
    """Import and return the shared LLM client functions."""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    from common.llm_client import chat, generate, check_ollama_running
    return chat, generate, check_ollama_running


def truncate_text(text: str, max_chars: int, notice: str = "[... Document truncated for analysis ...]") -> str:
    """Truncate text to max_chars with a notice appended."""
    if len(text) <= max_chars:
        return text
    logger.info("Truncating document from %d to %d chars", len(text), max_chars)
    return text[:max_chars] + f"\n\n{notice}"


def read_text_file(filepath: str) -> str:
    """Read and return contents of a plain text file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise ValueError(f"File is empty: {filepath}")

    return content


def read_pdf_file(filepath: str) -> str:
    """Extract text from a PDF file using PyPDF2.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If no text could be extracted.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        from PyPDF2 import PdfReader
    except ImportError:
        raise ImportError("PyPDF2 is required for PDF files. Install with: pip install PyPDF2")

    reader = PdfReader(filepath)
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)

    content = "\n".join(text_parts)
    if not content.strip():
        raise ValueError(f"Could not extract text from PDF: {filepath}")

    return content


def read_document(filepath: str) -> str:
    """Read a document file, supporting .txt and .pdf formats."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return read_pdf_file(filepath)
    else:
        return read_text_file(filepath)


def sanitize_for_markdown(text: str) -> str:
    """Basic sanitization for markdown export."""
    return text.replace("\r\n", "\n").strip()
