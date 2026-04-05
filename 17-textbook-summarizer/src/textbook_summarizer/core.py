"""Core business logic for the Textbook Summarizer."""

from typing import Optional, List, Dict, Any, Tuple, Union
import os
import re
import logging

from .utils import setup_sys_path, count_words, split_chapters

setup_sys_path()
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

STYLE_PROMPTS = {
    "concise": (
        "Summarize the following textbook chapter in a concise bullet-point format.\n"
        "Return your response in this exact structure:\n\n"
        "## Chapter Title\n"
        "Identify the chapter title and number if present.\n\n"
        "## Key Concepts\n"
        "- List each key concept as a short bullet point.\n\n"
        "## Definitions\n"
        "- **Term**: Brief definition (one sentence max).\n\n"
        "## Formulas & Equations\n"
        "- List any formulas or equations found. Write 'None found.' if there are none.\n\n"
        "## Summary\n"
        "A brief 3-5 sentence summary of the chapter.\n\n"
        "## Review Questions\n"
        "- Generate 3-5 short review questions based on the content.\n\n"
        "---\n"
        "Chapter text:\n\n{text}"
    ),
    "detailed": (
        "Provide a detailed, in-depth summary of the following textbook chapter.\n"
        "Return your response in this exact structure:\n\n"
        "## Chapter Title\n"
        "Identify the chapter title and number if present.\n\n"
        "## Key Concepts\n"
        "For each key concept, provide a full paragraph explanation with examples "
        "where relevant.\n\n"
        "## Definitions\n"
        "- **Term**: Full definition with context and usage examples.\n\n"
        "## Formulas & Equations\n"
        "- List any formulas or equations, explaining each variable and when to apply them. "
        "Write 'None found.' if there are none.\n\n"
        "## Summary\n"
        "A comprehensive summary covering all major points (8-12 sentences).\n\n"
        "## Review Questions\n"
        "- Generate 5-8 thought-provoking review questions, including both factual recall "
        "and critical thinking questions.\n\n"
        "---\n"
        "Chapter text:\n\n{text}"
    ),
    "study-guide": (
        "Create a study guide from the following textbook chapter in a flashcard-style "
        "question-and-answer format.\n"
        "Return your response in this exact structure:\n\n"
        "## Chapter Title\n"
        "Identify the chapter title and number if present.\n\n"
        "## Key Concepts (Q&A)\n"
        "For each key concept:\n"
        "- **Q:** A question about the concept.\n"
        "- **A:** A clear, concise answer.\n\n"
        "## Definitions (Flashcards)\n"
        "For each important term:\n"
        "- **Q:** What is [term]?\n"
        "- **A:** Definition and brief explanation.\n\n"
        "## Formulas & Equations\n"
        "- **Q:** What formula is used for [purpose]?\n"
        "- **A:** The formula with variable explanations. "
        "Write 'None found.' if there are none.\n\n"
        "## Summary\n"
        "A concise chapter summary suitable for quick review (4-6 sentences).\n\n"
        "## Practice Questions\n"
        "- 5-8 practice questions with answers, ranging from easy to challenging.\n\n"
        "---\n"
        "Chapter text:\n\n{text}"
    ),
}

SYSTEM_PROMPT = (
    "You are an expert academic tutor and textbook summarizer. "
    "You produce clear, accurate, and well-structured summaries that help "
    "students understand and review textbook material efficiently. "
    "Always preserve technical accuracy, especially for formulas and definitions."
)


def read_chapter_file(filepath: str) -> str:
    """Read and return the contents of a textbook chapter file.

    Args:
        filepath: Path to the text file containing the chapter.

    Returns:
        The chapter text as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def detect_chapter_info(text: str) -> str:
    """Attempt to detect chapter number and title from the text."""
    patterns = [
        r"(?i)^(chapter\s+\d+[\s:.\-]+.+)$",
        r"(?i)^(chapter\s+\d+)$",
        r"(?i)^(ch\.?\s*\d+[\s:.\-]+.+)$",
        r"(?i)^(unit\s+\d+[\s:.\-]+.+)$",
        r"(?i)^(lesson\s+\d+[\s:.\-]+.+)$",
    ]
    for line in text.strip().splitlines()[:10]:
        stripped = line.strip()
        for pattern in patterns:
            match = re.match(pattern, stripped)
            if match:
                return match.group(1).strip()
    return "Unknown Chapter"


def summarize_chapter(text: str, style: str = "concise", config: dict = None) -> str:
    """Generate a structured summary of a textbook chapter using the LLM.

    Args:
        text: The full text of the textbook chapter.
        style: Summary style — 'concise', 'detailed', or 'study-guide'.
        config: Optional configuration dictionary.

    Returns:
        The LLM-generated summary as a string.
    """
    if style not in STYLE_PROMPTS:
        raise ValueError(
            f"Invalid style '{style}'. Choose from: {', '.join(STYLE_PROMPTS)}"
        )

    config = config or {}
    llm_config = config.get("llm", {})
    prompt = STYLE_PROMPTS[style].format(text=text)

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=llm_config.get("temperature", 0.4),
        max_tokens=llm_config.get("max_tokens", 4096),
    )
    logger.info("Generated %s summary (%d chars)", style, len(response))
    return response


def summarize_multi_chapter(filepath: str, style: str = "concise", config: dict = None) -> list[dict]:
    """Summarize all chapters found in a multi-chapter textbook file.

    Args:
        filepath: Path to the textbook file.
        style: Summary style.
        config: Optional configuration.

    Returns:
        List of dicts with 'title' and 'summary' keys.
    """
    text = read_chapter_file(filepath)
    chapters = split_chapters(text)

    results = []
    for chapter in chapters:
        logger.info("Summarizing: %s", chapter["title"])
        summary = summarize_chapter(chapter["content"], style=style, config=config)
        results.append({
            "title": chapter["title"],
            "summary": summary,
            "word_count": count_words(chapter["content"]),
        })

    return results


def generate_glossary(text: str, config: dict = None) -> str:
    """Generate a key terms glossary from the chapter text.

    Args:
        text: Chapter text content.
        config: Optional configuration.

    Returns:
        Glossary as markdown string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    prompt = (
        "Extract all key terms and definitions from the following textbook content.\n"
        "Format as a glossary:\n"
        "- **Term**: Definition\n\n"
        "Content:\n\n" + text
    )

    return generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=llm_config.get("temperature", 0.3),
        max_tokens=llm_config.get("max_tokens", 2048),
    )


def generate_concept_map(text: str, config: dict = None) -> str:
    """Generate a concept map (as text) from chapter content.

    Args:
        text: Chapter text content.
        config: Optional configuration.

    Returns:
        Concept map as markdown string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    prompt = (
        "Create a concept map from the following textbook content.\n"
        "Show relationships between key concepts using this format:\n\n"
        "**Main Concept** → Related Concept 1, Related Concept 2\n"
        "**Related Concept 1** → Sub-concept A, Sub-concept B\n\n"
        "Content:\n\n" + text
    )

    return generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=llm_config.get("temperature", 0.3),
        max_tokens=llm_config.get("max_tokens", 2048),
    )


def generate_study_questions(text: str, num_questions: int = 5, config: dict = None) -> str:
    """Generate study/quiz questions from chapter content.

    Args:
        text: Chapter text content.
        num_questions: Number of questions to generate.
        config: Optional configuration.

    Returns:
        Study questions as markdown string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    prompt = (
        f"Generate {num_questions} study questions from the following textbook content.\n"
        "Include a mix of:\n"
        "- Multiple choice questions\n"
        "- Short answer questions\n"
        "- Critical thinking questions\n\n"
        "Provide answers for each question.\n\n"
        "Content:\n\n" + text
    )

    return generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=llm_config.get("temperature", 0.4),
        max_tokens=llm_config.get("max_tokens", 2048),
    )
