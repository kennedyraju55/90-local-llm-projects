#!/usr/bin/env python3
"""Core logic for Social Media Writer - post generation, validation, and formatting."""

import sys
import os
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration loading
# ---------------------------------------------------------------------------

_CONFIG_CACHE: Optional[dict] = None


def _find_config_path() -> str:
    """Locate config.yaml relative to the project root."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(project_root, "config.yaml")


def load_config(config_path: Optional[str] = None) -> dict:
    """Load configuration from config.yaml, with caching."""
    global _CONFIG_CACHE
    if _CONFIG_CACHE is not None and config_path is None:
        return _CONFIG_CACHE

    path = config_path or _find_config_path()
    try:
        with open(path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        logger.info("Loaded config from %s", path)
        if config_path is None:
            _CONFIG_CACHE = cfg
        return cfg
    except FileNotFoundError:
        logger.warning("Config file not found at %s, using defaults", path)
        return _default_config()


def _default_config() -> dict:
    """Return sensible defaults when config.yaml is absent."""
    return {
        "app": {"name": "Social Media Writer", "version": "2.0.0"},
        "llm": {"model": "llama3", "temperature": 0.8, "max_tokens": 2048},
        "platforms": {
            "twitter": {
                "max_chars": 280,
                "name": "Twitter/X",
                "hashtag_count": 3,
                "best_times": ["9:00 AM", "12:00 PM", "5:00 PM"],
            },
            "linkedin": {
                "max_chars": 3000,
                "name": "LinkedIn",
                "hashtag_count": 5,
                "best_times": ["7:30 AM", "12:00 PM", "5:30 PM"],
            },
            "instagram": {
                "max_chars": 2200,
                "name": "Instagram",
                "hashtag_count": 15,
                "best_times": ["11:00 AM", "2:00 PM", "7:00 PM"],
            },
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    }


def setup_logging(config: Optional[dict] = None) -> None:
    """Configure logging from the loaded config."""
    cfg = config or load_config()
    log_cfg = cfg.get("logging", {})
    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO")),
        format=log_cfg.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    )


# ---------------------------------------------------------------------------
# Constants (kept for backward compatibility)
# ---------------------------------------------------------------------------

PLATFORMS = ["twitter", "linkedin", "instagram"]
TONES = ["professional", "casual", "excited", "informative", "humorous"]

PLATFORM_CONFIG = {
    "twitter": {"max_chars": 280, "name": "Twitter/X", "hashtag_count": 3},
    "linkedin": {"max_chars": 3000, "name": "LinkedIn", "hashtag_count": 5},
    "instagram": {"max_chars": 2200, "name": "Instagram", "hashtag_count": 15},
}


def _get_platform_config(platform: str) -> dict:
    """Get platform config, preferring config.yaml when available."""
    try:
        cfg = load_config()
        platforms = cfg.get("platforms", {})
        if platform in platforms:
            return platforms[platform]
    except Exception:
        pass
    return PLATFORM_CONFIG[platform]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class SocialPost:
    """Represents a single social media post with metadata."""

    platform: str
    content: str
    hashtags: list[str] = field(default_factory=list)
    char_count: int = 0
    is_within_limit: bool = True
    tone: str = "professional"
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Post init."""
        self.char_count = len(self.content)
        config = _get_platform_config(self.platform)
        self.is_within_limit = self.char_count <= config["max_chars"]
        if not self.hashtags:
            self.hashtags = _extract_hashtags(self.content)


def _extract_hashtags(content: str) -> list[str]:
    """Extract hashtag strings from post content."""
    return re.findall(r"#\w+", content)


# ---------------------------------------------------------------------------
# Prompt building & generation (existing, enhanced)
# ---------------------------------------------------------------------------


def build_prompt(platform: str, topic: str, tone: str, variants: int) -> str:
    """Build the social media post generation prompt."""
    config = _get_platform_config(platform)
    return (
        f"Create {variants} {config['name']} post(s) about: {topic}\n\n"
        f"Requirements:\n"
        f"- Platform: {config['name']}\n"
        f"- Maximum character limit: {config['max_chars']} characters\n"
        f"- Tone: {tone}\n"
        f"- Include {config['hashtag_count']} relevant hashtags\n"
        f"- Each post should be engaging and shareable\n"
        f"- For Twitter: keep it concise and punchy\n"
        f"- For LinkedIn: be professional with a hook and CTA\n"
        f"- For Instagram: be visual-oriented with emoji usage\n"
        f"- Label each variant as 'Variant 1:', 'Variant 2:', etc.\n"
        f"- Add hashtags at the end of each post\n"
    )


def generate_posts(platform: str, topic: str, tone: str, variants: int) -> str:
    """Generate social media posts using the LLM."""
    logger.info("Generating %d %s post(s) about '%s' with tone '%s'", variants, platform, topic, tone)
    system_prompt = (
        "You are a social media marketing expert. You create viral, engaging posts "
        "tailored to each platform's best practices and audience expectations. "
        "Always respect character limits and platform norms."
    )
    user_prompt = build_prompt(platform, topic, tone, variants)
    messages = [{"role": "user", "content": user_prompt}]

    cfg = load_config()
    llm_cfg = cfg.get("llm", {})
    result = chat(
        messages,
        system_prompt=system_prompt,
        temperature=llm_cfg.get("temperature", 0.8),
        max_tokens=llm_cfg.get("max_tokens", 2048),
    )
    logger.info("Post generation complete (%d chars returned)", len(result))
    return result


# ---------------------------------------------------------------------------
# New functions
# ---------------------------------------------------------------------------


def validate_char_count(content: str, platform: str) -> tuple[bool, int, int]:
    """
    Check whether *content* fits within the platform's character limit.

    Returns:
        (is_valid, char_count, platform_limit)
    """
    config = _get_platform_config(platform)
    limit = config["max_chars"]
    count = len(content)
    is_valid = count <= limit
    logger.debug("Char validation for %s: %d/%d (valid=%s)", platform, count, limit, is_valid)
    return is_valid, count, limit


def generate_hashtags(topic: str, platform: str, count: Optional[int] = None) -> str:
    """Generate relevant hashtags for a topic on a given platform via the LLM."""
    config = _get_platform_config(platform)
    num = count or config["hashtag_count"]
    logger.info("Generating %d hashtags for '%s' on %s", num, topic, platform)

    messages = [
        {
            "role": "user",
            "content": (
                f"Generate exactly {num} trending and relevant hashtags for the topic: '{topic}' "
                f"on {config['name']}.\n\n"
                f"Return ONLY the hashtags, one per line, each starting with #.\n"
                f"Make them specific, popular, and relevant to the topic."
            ),
        }
    ]
    return chat(
        messages,
        system_prompt="You are a social media hashtag expert. Generate only hashtags, nothing else.",
        temperature=0.7,
        max_tokens=256,
    )


def suggest_schedule(platform: str) -> list[str]:
    """Return the best posting times for a platform from config."""
    config = _get_platform_config(platform)
    times = config.get("best_times", [])
    if not times:
        defaults = {
            "twitter": ["9:00 AM", "12:00 PM", "5:00 PM"],
            "linkedin": ["7:30 AM", "12:00 PM", "5:30 PM"],
            "instagram": ["11:00 AM", "2:00 PM", "7:00 PM"],
        }
        times = defaults.get(platform, ["9:00 AM", "12:00 PM", "5:00 PM"])
    logger.info("Suggested schedule for %s: %s", platform, times)
    return times


def generate_ab_variants(
    topic: str,
    platform: str,
    tone: str,
    num_variants: int = 2,
) -> str:
    """Generate A/B test post variants with distinct approaches."""
    config = _get_platform_config(platform)
    logger.info("Generating %d A/B variants for '%s' on %s", num_variants, topic, platform)

    messages = [
        {
            "role": "user",
            "content": (
                f"Create {num_variants} distinctly different A/B test variants of a {config['name']} post "
                f"about: {topic}\n\n"
                f"Requirements:\n"
                f"- Platform: {config['name']} (max {config['max_chars']} chars)\n"
                f"- Tone: {tone}\n"
                f"- Include {config['hashtag_count']} hashtags per variant\n"
                f"- Each variant should use a DIFFERENT approach:\n"
                f"  * Variant A: Question-based hook\n"
                f"  * Variant B: Statement/bold-claim hook\n"
                f"  * Additional variants: Story-based, Data-driven, etc.\n"
                f"- Label each as 'Variant A:', 'Variant B:', etc.\n"
                f"- After each variant, add a note on why that approach might work.\n"
            ),
        }
    ]
    return chat(
        messages,
        system_prompt=(
            "You are a social media A/B testing expert. Create meaningfully different "
            "variants that test distinct messaging strategies."
        ),
        temperature=0.9,
        max_tokens=2048,
    )


def format_for_platform(content: str, platform: str) -> str:
    """
    Format content according to platform conventions.

    - Twitter:   compact, no excess whitespace
    - LinkedIn:  professional paragraphs with line breaks
    - Instagram: emoji-enriched with spacing
    """
    if platform == "twitter":
        content = " ".join(content.split())
        config = _get_platform_config(platform)
        if len(content) > config["max_chars"]:
            content = content[: config["max_chars"] - 3] + "..."
        return content

    if platform == "linkedin":
        paragraphs = [p.strip() for p in content.split("\n") if p.strip()]
        return "\n\n".join(paragraphs)

    if platform == "instagram":
        if not any(c in content for c in "✨🚀💡🔥❤️📸🎉"):
            content = f"✨ {content}"
        paragraphs = [p.strip() for p in content.split("\n") if p.strip()]
        formatted = "\n\n".join(paragraphs)
        hashtags = _extract_hashtags(formatted)
        if hashtags:
            body = re.sub(r"#\w+\s*", "", formatted).strip()
            tag_block = " ".join(hashtags)
            formatted = f"{body}\n\n.\n.\n.\n{tag_block}"
        return formatted

    return content


def preview_post(content: str, platform: str) -> dict:
    """
    Return a preview dict with metrics about the post.

    Keys: char_count, is_valid, hashtag_count, estimated_reach_score
    """
    config = _get_platform_config(platform)
    char_count = len(content)
    limit = config["max_chars"]
    hashtags = _extract_hashtags(content)
    hashtag_count = len(hashtags)

    # Simple heuristic reach score (0-100)
    score = 50
    # Hashtags boost reach
    ideal_tags = config["hashtag_count"]
    if hashtag_count >= ideal_tags:
        score += 15
    elif hashtag_count > 0:
        score += 5

    # Being within char limit is important
    if char_count <= limit:
        score += 10
        # Optimal length boosts score further
        ratio = char_count / limit
        if 0.7 <= ratio <= 0.95:
            score += 15
        elif 0.5 <= ratio < 0.7:
            score += 10
    else:
        score -= 20

    # Emoji presence (especially for Instagram)
    has_emoji = bool(re.search(r"[^\w\s#@.,!?;:\-\"\'()/\\]", content))
    if platform == "instagram" and has_emoji:
        score += 10
    elif has_emoji:
        score += 5

    score = max(0, min(100, score))

    return {
        "char_count": char_count,
        "is_valid": char_count <= limit,
        "hashtag_count": hashtag_count,
        "estimated_reach_score": score,
    }
