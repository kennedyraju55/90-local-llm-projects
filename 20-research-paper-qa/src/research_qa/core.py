"""Core business logic for the Research Paper QA."""

from typing import Optional, List, Dict, Any, Tuple, Union
import os
import logging

from .utils import setup_sys_path

setup_sys_path()
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

SYSTEM_PROMPT_TEMPLATE = """You are a research paper analysis assistant. You have been given the full text of research paper(s) below. Answer questions accurately based on the paper's content. If the answer is not found in the paper, say so clearly.

When answering:
- Cite specific sections or findings from the paper when possible
- Be precise and academic in tone
- For complex questions, break down the answer into clear parts
- If asked about methodology, results, or conclusions, refer directly to what the paper states
- When citing, use [Paper: filename, Section: X] format

--- PAPER CONTENT ---
{paper_content}
--- END OF PAPER ---"""

FOLLOWUP_PROMPT = (
    "Based on the conversation so far about the research paper, "
    "suggest {n} follow-up questions the user might want to ask. "
    "Format as a numbered list. Make them specific and insightful."
)


def load_paper(paper_path: str) -> str:
    """Load and return the contents of a research paper text file.

    Args:
        paper_path: Path to the paper text file.

    Returns:
        The full text content of the paper.

    Raises:
        FileNotFoundError: If the paper file does not exist.
        ValueError: If the paper file is empty.
    """
    if not os.path.exists(paper_path):
        raise FileNotFoundError(f"Paper not found: {paper_path}")

    with open(paper_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise ValueError(f"Paper file is empty: {paper_path}")

    logger.info("Loaded paper: %s (%d words)", paper_path, len(content.split()))
    return content


def load_multiple_papers(paper_paths: list[str]) -> dict[str, str]:
    """Load multiple research papers.

    Args:
        paper_paths: List of file paths to paper text files.

    Returns:
        Dictionary mapping filenames to content strings.
    """
    papers = {}
    for path in paper_paths:
        content = load_paper(path)
        filename = os.path.basename(path)
        papers[filename] = content
        logger.info("Loaded: %s", filename)
    return papers


def build_system_prompt(paper_content: str) -> str:
    """Build the system prompt with the paper content embedded.

    Args:
        paper_content: The full text of the research paper(s).

    Returns:
        Formatted system prompt string.
    """
    return SYSTEM_PROMPT_TEMPLATE.format(paper_content=paper_content)


def build_multi_paper_content(papers: dict[str, str]) -> str:
    """Build combined content from multiple papers.

    Args:
        papers: Dictionary mapping filenames to content.

    Returns:
        Combined paper content with separators.
    """
    parts = []
    for filename, content in papers.items():
        parts.append(f"=== Paper: {filename} ===\n\n{content}\n\n")
    return "\n".join(parts)


def ask_question(
    question: str,
    conversation_history: list[dict],
    system_prompt: str,
    config: dict = None,
) -> str:
    """Send a question to the LLM with full conversation context.

    Args:
        question: The user's question about the paper.
        conversation_history: List of previous message dicts for context.
        system_prompt: The system prompt containing the paper content.
        config: Optional configuration dictionary.

    Returns:
        The LLM's response string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    conversation_history.append({"role": "user", "content": question})

    response = chat(
        messages=conversation_history,
        system_prompt=system_prompt,
        temperature=llm_config.get("temperature", 0.3),
        max_tokens=llm_config.get("max_tokens", 2048),
    )

    conversation_history.append({"role": "assistant", "content": response})
    logger.info("Question answered (%d chars)", len(response))
    return response


def suggest_followup_questions(
    conversation_history: list[dict],
    system_prompt: str,
    num_suggestions: int = 3,
    config: dict = None,
) -> str:
    """Generate follow-up question suggestions based on conversation.

    Args:
        conversation_history: Current conversation history.
        system_prompt: System prompt with paper content.
        num_suggestions: Number of suggestions to generate.
        config: Optional configuration.

    Returns:
        Follow-up suggestions as a string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    prompt = FOLLOWUP_PROMPT.format(n=num_suggestions)
    messages = conversation_history + [{"role": "user", "content": prompt}]

    return chat(
        messages=messages,
        system_prompt=system_prompt,
        temperature=llm_config.get("temperature", 0.5),
        max_tokens=512,
    )


def extract_citations(answer: str) -> list[str]:
    """Extract citation references from an answer.

    Args:
        answer: The LLM's answer text.

    Returns:
        List of citation strings found.
    """
    import re
    pattern = r'\[Paper:.*?\]|\[Section:.*?\]|\[.*?et al\..*?\]'
    return re.findall(pattern, answer)
