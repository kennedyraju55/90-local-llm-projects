"""Core business logic for the News Digest Generator."""

from typing import Optional, List, Dict, Any, Tuple, Union
import os
import glob as glob_module
import logging
from datetime import datetime

from .utils import setup_sys_path, format_digest_header

setup_sys_path()
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)


def read_news_files(sources_dir: str) -> list[dict]:
    """Read all .txt files from the sources directory.

    Args:
        sources_dir: Path to folder containing .txt news files.

    Returns:
        List of dicts with 'filename' and 'content' keys.

    Raises:
        FileNotFoundError: If the sources directory does not exist.
        ValueError: If no .txt files are found in the directory.
    """
    if not os.path.isdir(sources_dir):
        raise FileNotFoundError(f"Sources directory not found: {sources_dir}")

    pattern = os.path.join(sources_dir, "*.txt")
    files = sorted(glob_module.glob(pattern))

    if not files:
        raise ValueError(f"No .txt files found in: {sources_dir}")

    articles = []
    for filepath in files:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read().strip()
        if content:
            articles.append({
                "filename": os.path.basename(filepath),
                "content": content,
            })

    if not articles:
        raise ValueError(f"All .txt files in '{sources_dir}' are empty.")

    logger.info("Read %d articles from %s", len(articles), sources_dir)
    return articles


def categorize_articles(articles: list[dict], num_topics: int, config: dict = None) -> str:
    """Send articles to the LLM for topic categorization.

    Args:
        articles: List of article dicts with 'filename' and 'content'.
        num_topics: Desired number of topic groups.
        config: Optional configuration dictionary.

    Returns:
        Raw LLM response with categorized articles.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    articles_text = "\n\n---\n\n".join(
        f"[File: {a['filename']}]\n{a['content']}" for a in articles
    )

    categories = config.get("digest", {}).get("categories", [])
    category_hint = ""
    if categories:
        category_hint = f"\nSuggested categories (use if applicable): {', '.join(categories)}\n"

    prompt = (
        f"You are a news editor. Below are {len(articles)} news articles. "
        f"Group them into exactly {num_topics} topic categories.\n"
        f"{category_hint}\n"
        f"For each topic category:\n"
        f"1. Give the topic a clear, concise name\n"
        f"2. List which articles (by filename) belong to it\n"
        f"3. Write a 2-3 sentence summary of that topic group\n"
        f"4. Tag each article with a category label\n\n"
        f"Format your response as:\n\n"
        f"## Topic: <topic name>\n"
        f"**Category:** <category>\n"
        f"**Articles:** <comma-separated filenames>\n"
        f"**Summary:** <summary text>\n\n"
        f"ARTICLES:\n\n{articles_text}"
    )

    return generate(
        prompt=prompt,
        system_prompt="You are a professional news editor who categorizes and summarizes news articles.",
        temperature=llm_config.get("temperature", 0.4),
        max_tokens=llm_config.get("max_tokens", 4096),
    )


def generate_digest(articles: list[dict], categorization: str, digest_format: str = "daily", config: dict = None) -> str:
    """Generate an overall news digest from the categorized articles.

    Args:
        articles: List of article dicts.
        categorization: LLM-generated categorization text.
        digest_format: 'daily' or 'weekly'.
        config: Optional configuration.

    Returns:
        Raw LLM response with the full news digest.
    """
    config = config or {}
    llm_config = config.get("llm", {})
    enable_sentiment = config.get("digest", {}).get("enable_sentiment", True)
    enable_trends = config.get("digest", {}).get("enable_trends", True)

    sections = [
        "1. **Key Headlines** — the 3-5 most important headlines",
        "2. **Topic Summaries** — a polished paragraph for each topic group",
    ]
    if enable_sentiment:
        sections.append("3. **Sentiment Analysis** — overall sentiment (positive/negative/neutral) for each topic")
    if enable_trends:
        sections.append(f"{len(sections)+1}. **Trending Themes** — overarching themes and emerging trends")
    sections.append(f"{len(sections)+1}. **Outlook** — a brief forward-looking paragraph")

    sections_text = "\n".join(sections)

    prompt = (
        f"Based on the following topic categorization of {len(articles)} news articles, "
        f"generate a professional {digest_format} news digest.\n\n"
        f"The digest should include:\n{sections_text}\n\n"
        f"CATEGORIZATION:\n\n{categorization}"
    )

    return generate(
        prompt=prompt,
        system_prompt="You are a professional news digest writer producing concise, informative summaries.",
        temperature=llm_config.get("temperature", 0.5),
        max_tokens=llm_config.get("max_tokens", 4096),
    )


def analyze_sentiment(articles: list[dict], config: dict = None) -> str:
    """Analyze sentiment across articles.

    Args:
        articles: List of article dicts.
        config: Optional configuration.

    Returns:
        Sentiment analysis as markdown string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    articles_text = "\n\n".join(
        f"[{a['filename']}]: {a['content'][:500]}" for a in articles
    )

    prompt = (
        "Analyze the sentiment of each news article below.\n"
        "For each article, provide:\n"
        "- **Filename**: sentiment (Positive/Negative/Neutral) - brief explanation\n\n"
        "Then provide an overall sentiment summary.\n\n"
        f"ARTICLES:\n\n{articles_text}"
    )

    return generate(
        prompt=prompt,
        system_prompt="You are a sentiment analysis expert for news articles.",
        temperature=llm_config.get("temperature", 0.3),
        max_tokens=llm_config.get("max_tokens", 2048),
    )


def save_output(filepath: str, categorization: str, digest: str) -> None:
    """Save the digest output to a file.

    Args:
        filepath: Destination file path.
        categorization: LLM categorization text.
        digest: LLM digest text.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# News Digest\n\n")
        f.write("## Topic Categorization\n\n")
        f.write(categorization)
        f.write("\n\n---\n\n")
        f.write("## Full Digest\n\n")
        f.write(digest)
        f.write("\n")
    logger.info("Digest saved to %s", filepath)
