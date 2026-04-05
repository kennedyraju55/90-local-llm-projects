#!/usr/bin/env python3
"""Core logic for Blog Post Generator."""

import sys
import os
import re
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running  # noqa: E402

logger = logging.getLogger(__name__)

TONES = ["professional", "casual", "technical", "friendly", "persuasive"]

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_config_cache: Optional[dict] = None


def _find_config_path() -> str:
    """Locate config.yaml relative to the project root."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "..", "..", "..", "config.yaml"),
        os.path.join(here, "..", "..", "config.yaml"),
        os.path.join(os.getcwd(), "config.yaml"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return os.path.abspath(path)
    return candidates[0]


def load_config(path: Optional[str] = None) -> dict:
    """Load configuration from a YAML file.

    Falls back to sensible defaults when the file is not found.
    """
    global _config_cache
    if _config_cache is not None and path is None:
        return _config_cache

    if path is None:
        path = _find_config_path()

    defaults: dict = {
        "app": {"name": "Blog Post Generator", "version": "2.0.0"},
        "llm": {"model": "llama3", "temperature": 0.7, "max_tokens": 2400},
        "blog": {
            "default_tone": "professional",
            "default_length": 800,
            "max_drafts": 5,
            "seo": {
                "min_keyword_density": 0.01,
                "max_keyword_density": 0.03,
                "min_word_count": 300,
            },
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    }

    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        logger.info("Loaded config from %s", path)
    except FileNotFoundError:
        logger.warning("Config file not found at %s – using defaults", path)
        data = {}

    def _merge(base: dict, override: dict) -> dict:
        merged = base.copy()
        for key, val in override.items():
            """Merge."""
            if isinstance(val, dict) and isinstance(merged.get(key), dict):
                merged[key] = _merge(merged[key], val)
            else:
                merged[key] = val
        return merged

    result = _merge(defaults, data)

    if path is None or path == _find_config_path():
        _config_cache = result

    return result


def setup_logging(config: Optional[dict] = None) -> None:
    """Configure the root logger based on *config*."""
    if config is None:
        config = load_config()
    log_cfg = config.get("logging", {})
    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO")),
        format=log_cfg.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    )


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class BlogPost:
    """Represents a generated blog post with metadata."""

    title: str
    content: str
    meta_description: str = ""
    keywords: list[str] = field(default_factory=list)
    tone: str = "professional"
    seo_score: float = 0.0
    word_count: int = 0
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def __post_init__(self) -> None:
        if self.word_count == 0:
            """Post init."""
            self.word_count = len(self.content.split())


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------


def build_prompt(topic: str, keywords: list[str], tone: str, length: int) -> str:
    """Build the blog post generation prompt."""
    kw_str = ", ".join(keywords) if keywords else "none specified"
    return (
        f"Write a {length}-word SEO-friendly blog post about: {topic}\n\n"
        f"Requirements:\n"
        f"- Tone: {tone}\n"
        f"- Target keywords to include naturally: {kw_str}\n"
        f"- Include an engaging title (prefixed with '# ')\n"
        f"- Include a meta description (1-2 sentences, prefixed with '> ')\n"
        f"- Use proper markdown headings (##, ###) for sections\n"
        f"- Include an introduction, 3-4 main sections, and a conclusion\n"
        f"- Optimize for SEO with keyword placement in headings and first paragraphs\n"
        f"- Approximate length: {length} words\n"
    )


def _build_outline_prompt(topic: str, keywords: list[str], tone: str) -> str:
    """Build a prompt that asks the LLM for an outline only."""
    kw_str = ", ".join(keywords) if keywords else "none specified"
    return (
        f"Create a detailed outline for a blog post about: {topic}\n\n"
        f"Requirements:\n"
        f"- Tone: {tone}\n"
        f"- Target keywords: {kw_str}\n"
        f"- Provide a suggested title (prefixed with '# ')\n"
        f"- Provide a meta description (prefixed with '> ')\n"
        f"- List 4-6 section headings (prefixed with '## ')\n"
        f"- Under each heading, add 2-3 bullet points describing key content\n"
        f"- Output in markdown format\n"
    )


# ---------------------------------------------------------------------------
# Generation helpers
# ---------------------------------------------------------------------------


def generate_blog_post(topic: str, keywords: list[str], tone: str, length: int) -> str:
    """Generate a blog post using the LLM."""
    logger.info("Generating blog post – topic=%s, tone=%s, length=%d", topic, tone, length)
    config = load_config()
    llm_cfg = config.get("llm", {})

    system_prompt = (
        "You are an expert content writer and SEO specialist. "
        "You write engaging, well-structured blog posts optimized for search engines. "
        "Always output in clean markdown format."
    )
    user_prompt = build_prompt(topic, keywords, tone, length)
    messages = [{"role": "user", "content": user_prompt}]

    result = chat(
        messages,
        system_prompt=system_prompt,
        temperature=llm_cfg.get("temperature", 0.7),
        max_tokens=llm_cfg.get("max_tokens", length * 3),
    )
    logger.info("Blog post generated – %d words", len(result.split()))
    return result


def generate_outline(topic: str, keywords: list[str], tone: str) -> str:
    """Generate an outline preview before creating the full post."""
    logger.info("Generating outline – topic=%s", topic)
    system_prompt = (
        "You are an expert content strategist. "
        "Create clear, well-structured outlines for blog posts."
    )
    user_prompt = _build_outline_prompt(topic, keywords, tone)
    messages = [{"role": "user", "content": user_prompt}]
    result = chat(messages, system_prompt=system_prompt, temperature=0.5, max_tokens=800)
    logger.info("Outline generated")
    return result


def generate_multiple_drafts(
    topic: str,
    keywords: list[str],
    tone: str,
    length: int,
    num_drafts: int = 3,
) -> list[str]:
    """Generate *num_drafts* alternative drafts for the same topic.

    Each draft uses a slightly different temperature to introduce variation.
    """
    config = load_config()
    max_drafts = config.get("blog", {}).get("max_drafts", 5)
    num_drafts = min(num_drafts, max_drafts)
    logger.info("Generating %d drafts – topic=%s", num_drafts, topic)

    system_prompt = (
        "You are an expert content writer and SEO specialist. "
        "You write engaging, well-structured blog posts optimized for search engines. "
        "Always output in clean markdown format."
    )
    user_prompt = build_prompt(topic, keywords, tone, length)

    drafts: list[str] = []
    base_temp = 0.6
    for i in range(num_drafts):
        temp = min(base_temp + i * 0.1, 1.0)
        messages = [{"role": "user", "content": user_prompt}]
        draft = chat(
            messages,
            system_prompt=system_prompt,
            temperature=temp,
            max_tokens=length * 3,
        )
        drafts.append(draft)
        logger.info("Draft %d/%d generated (%d words)", i + 1, num_drafts, len(draft.split()))

    return drafts


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------


def score_seo(content: str, keywords: list[str]) -> dict:
    """Score the SEO quality of *content* on a 0-100 scale.

    Returns a dict with the total score and per-criterion breakdown:
    - keyword_density: Are keywords used at the right frequency?
    - heading_structure: Does the post have proper heading hierarchy?
    - meta_description: Is a meta description present?
    - content_length: Is the content long enough?
    """
    config = load_config()
    seo_cfg = config.get("blog", {}).get("seo", {})
    min_density = seo_cfg.get("min_keyword_density", 0.01)
    max_density = seo_cfg.get("max_keyword_density", 0.03)
    min_words = seo_cfg.get("min_word_count", 300)

    scores: dict[str, float] = {}
    content_lower = content.lower()
    words = content_lower.split()
    word_count = len(words)

    # 1. Keyword density (30 pts)
    if keywords:
        densities: list[float] = []
        for kw in keywords:
            kw_lower = kw.lower()
            count = content_lower.count(kw_lower)
            density = count / max(word_count, 1)
            densities.append(density)

        avg_density = sum(densities) / len(densities)
        if min_density <= avg_density <= max_density:
            scores["keyword_density"] = 30.0
        elif avg_density > 0:
            ratio = min(avg_density / min_density, 1.0)
            scores["keyword_density"] = round(30.0 * ratio, 1)
        else:
            scores["keyword_density"] = 0.0
    else:
        scores["keyword_density"] = 15.0  # neutral when no keywords specified

    # 2. Heading structure (25 pts)
    has_h1 = bool(re.search(r"^# ", content, re.MULTILINE))
    h2_count = len(re.findall(r"^## ", content, re.MULTILINE))
    heading_score = 0.0
    if has_h1:
        heading_score += 10.0
    if h2_count >= 3:
        heading_score += 15.0
    elif h2_count >= 1:
        heading_score += 8.0
    scores["heading_structure"] = heading_score

    # 3. Meta description (20 pts)
    has_meta = bool(re.search(r"^> ", content, re.MULTILINE))
    scores["meta_description"] = 20.0 if has_meta else 0.0

    # 4. Content length (25 pts)
    if word_count >= min_words:
        scores["content_length"] = 25.0
    else:
        scores["content_length"] = round(25.0 * (word_count / min_words), 1)

    total = round(sum(scores.values()), 1)

    logger.info("SEO score: %.1f (keywords=%.1f, headings=%.1f, meta=%.1f, length=%.1f)",
                total, scores["keyword_density"], scores["heading_structure"],
                scores["meta_description"], scores["content_length"])

    return {"total": total, **scores}


def analyze_tone(content: str) -> dict:
    """Heuristic tone analysis of *content*.

    Returns a dict mapping tone labels to confidence scores (0-1).
    """
    logger.info("Analyzing tone of content (%d words)", len(content.split()))

    content_lower = content.lower()

    professional_markers = [
        "furthermore", "therefore", "consequently", "significant",
        "implement", "strategy", "objective", "comprehensive",
        "leverage", "optimize", "facilitate", "establish",
    ]
    casual_markers = [
        "you", "your", "let's", "awesome", "cool", "hey",
        "gonna", "wanna", "pretty", "stuff", "thing", "right?",
    ]
    technical_markers = [
        "algorithm", "implementation", "architecture", "framework",
        "configure", "deploy", "api", "database", "function",
        "parameter", "module", "protocol",
    ]
    friendly_markers = [
        "we", "our", "together", "welcome", "glad", "excited",
        "happy", "enjoy", "wonderful", "fantastic", "love",
    ]
    persuasive_markers = [
        "must", "need", "should", "imagine", "transform",
        "proven", "guarantee", "essential", "critical", "act now",
        "don't miss", "limited",
    ]

    def _score(markers: list[str]) -> float:
        """Score."""
        count = sum(1 for m in markers if m in content_lower)
        return round(min(count / max(len(markers) * 0.4, 1), 1.0), 2)

    result = {
        "professional": _score(professional_markers),
        "casual": _score(casual_markers),
        "technical": _score(technical_markers),
        "friendly": _score(friendly_markers),
        "persuasive": _score(persuasive_markers),
    }

    dominant = max(result, key=result.get)  # type: ignore[arg-type]
    result["dominant_tone"] = dominant
    logger.info("Tone analysis complete – dominant=%s", dominant)
    return result


# ---------------------------------------------------------------------------
# Export helpers
# ---------------------------------------------------------------------------


def _extract_title(content: str) -> str:
    """Extract the first H1 heading from markdown *content*."""
    match = re.search(r"^# (.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def _extract_meta_description(content: str) -> str:
    """Extract the first blockquote line used as meta description."""
    match = re.search(r"^> (.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def export_markdown(content: str, filepath: str, keywords: Optional[list[str]] = None) -> str:
    """Export *content* to a markdown file with YAML frontmatter.

    Returns the absolute path of the written file.
    """
    title = _extract_title(content)
    seo = score_seo(content, keywords or [])

    frontmatter = (
        "---\n"
        f"title: \"{title}\"\n"
        f"date: \"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}\"\n"
        f"keywords: {keywords or []}\n"
        f"seo_score: {seo['total']}\n"
        "---\n\n"
    )

    full_content = frontmatter + content

    abs_path = os.path.abspath(filepath)
    os.makedirs(os.path.dirname(abs_path) or ".", exist_ok=True)
    with open(abs_path, "w", encoding="utf-8") as fh:
        fh.write(full_content)

    logger.info("Exported markdown to %s", abs_path)
    return abs_path


def parse_blog_post(content: str, keywords: Optional[list[str]] = None, tone: str = "professional") -> BlogPost:
    """Parse raw LLM output into a structured *BlogPost*."""
    title = _extract_title(content)
    meta = _extract_meta_description(content)
    kw = keywords or []
    seo = score_seo(content, kw)

    return BlogPost(
        title=title,
        content=content,
        meta_description=meta,
        keywords=kw,
        tone=tone,
        seo_score=seo["total"],
    )
