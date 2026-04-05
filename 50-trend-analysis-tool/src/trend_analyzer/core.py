#!/usr/bin/env python3
"""Core business logic for the Trend Analysis Tool.

Provides topic extraction, sentiment analysis, topic evolution tracking,
emerging topic detection, and report generation using a local LLM.
"""

import json
import logging
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "model": {"name": "gemma3", "temperature": 0.3, "max_tokens": 4000},
    "file_extensions": [".txt", ".md", ".text", ".csv", ".log"],
    "analysis": {"max_documents": 50, "preview_chars": 500, "topic_limit": 20},
    "emerging_detection": {"threshold": 0.7, "min_frequency": "medium"},
    "sentiment": {"enabled": True, "granularity": "document"},
    "schedule": {
        "enabled": False,
        "frequency": "weekly",
        "day": "monday",
        "time": "09:00",
    },
    "logging": {"level": "INFO", "file": "trend_analyzer.log"},
}


def load_config(path: Optional[str] = None) -> dict:
    """Load configuration from a YAML file, falling back to defaults.

    Args:
        path: Path to a YAML config file. If ``None``, returns defaults.

    Returns:
        Merged configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()
    if path is None:
        logger.debug("No config path provided, using defaults")
        return config

    config_path = Path(path)
    if not config_path.exists():
        logger.warning("Config file '%s' not found, using defaults", path)
        return config

    try:
        with open(config_path, "r", encoding="utf-8") as fh:
            user_config = yaml.safe_load(fh) or {}
        _deep_merge(config, user_config)
        logger.info("Loaded config from '%s'", path)
    except (yaml.YAMLError, OSError) as exc:
        logger.error("Failed to load config '%s': %s", path, exc)

    return config


def _deep_merge(base: dict, override: dict) -> None:
    """Recursively merge *override* into *base* in-place."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value


def setup_logging(config: dict) -> None:
    """Configure the logging subsystem from *config*."""
    log_cfg = config.get("logging", {})
    level = getattr(logging, log_cfg.get("level", "INFO").upper(), logging.INFO)
    log_file = log_cfg.get("file")

    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )
    logger.debug("Logging configured: level=%s file=%s", level, log_file)


# ---------------------------------------------------------------------------
# Document loading
# ---------------------------------------------------------------------------

def load_text_files(directory: str, config: Optional[dict] = None) -> list[dict]:
    """Load text files from *directory*.

    Args:
        directory: Path to a folder containing text documents.
        config: Optional config dict (uses ``file_extensions`` /
                ``analysis.max_documents`` keys).

    Returns:
        List of document dicts with keys ``filename``, ``content``,
        ``size``, and ``modified``.

    Raises:
        FileNotFoundError: If *directory* does not exist.
        ValueError: If no readable text files are found.
    """
    config = config or DEFAULT_CONFIG
    dir_path = Path(directory)

    if not dir_path.exists():
        logger.error("Directory '%s' not found", directory)
        raise FileNotFoundError(f"Directory '{directory}' not found.")

    extensions = set(config.get("file_extensions", DEFAULT_CONFIG["file_extensions"]))
    max_docs = config.get("analysis", {}).get(
        "max_documents", DEFAULT_CONFIG["analysis"]["max_documents"]
    )

    documents: list[dict] = []
    for file_path in sorted(dir_path.iterdir()):
        if not file_path.is_file() or file_path.suffix.lower() not in extensions:
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
            if content.strip():
                documents.append(
                    {
                        "filename": file_path.name,
                        "content": content,
                        "size": len(content),
                        "modified": os.path.getmtime(str(file_path)),
                    }
                )
        except (UnicodeDecodeError, PermissionError) as exc:
            logger.warning("Skipping '%s': %s", file_path.name, exc)
            continue

    if not documents:
        logger.error("No readable text files in '%s'", directory)
        raise ValueError(f"No readable text files found in '{directory}'.")

    documents = documents[:max_docs]
    logger.info("Loaded %d documents from '%s'", len(documents), directory)
    return documents


# ---------------------------------------------------------------------------
# LLM helpers
# ---------------------------------------------------------------------------

def _parse_json_response(response: str) -> Optional[dict]:
    """Try to extract a JSON object from an LLM response string."""
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError) as exc:
        logger.debug("JSON parse failed: %s", exc)
    return None


def _model_kwargs(config: Optional[dict] = None) -> dict:
    """Return common keyword arguments for ``chat()``."""
    config = config or DEFAULT_CONFIG
    model_cfg = config.get("model", DEFAULT_CONFIG["model"])
    return {
        "model": model_cfg.get("name", "gemma3"),
        "temperature": model_cfg.get("temperature", 0.3),
        "max_tokens": model_cfg.get("max_tokens", 4000),
    }


# ---------------------------------------------------------------------------
# Topic extraction
# ---------------------------------------------------------------------------

def extract_topics(documents: list[dict], config: Optional[dict] = None) -> dict:
    """Extract topics and trends from *documents* via LLM.

    Returns:
        Dict with ``topics`` list and ``overall_theme`` string.
    """
    config = config or DEFAULT_CONFIG
    preview_chars = config.get("analysis", {}).get("preview_chars", 500)
    topic_limit = config.get("analysis", {}).get("topic_limit", 20)

    doc_summaries = [
        f"[{doc['filename']}]: {doc['content'][:preview_chars]}"
        for doc in documents[:topic_limit]
    ]
    combined = "\n\n".join(doc_summaries)

    system_prompt = (
        "You are a trend analysis expert. Identify the key topics and emerging "
        "trends from the provided documents. Respond ONLY with valid JSON:\n"
        '{"topics": [{"name": "topic", "frequency": "high|medium|low", '
        '"trend": "emerging|growing|stable|declining", '
        '"description": "brief description", "related_docs": ["file1.txt"]}], '
        '"overall_theme": "main theme description"}'
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Analyze these {len(documents)} documents for trends and "
                f"topics:\n\n{combined}"
            ),
        }
    ]

    kwargs = _model_kwargs(config)
    logger.info("Extracting topics from %d documents", len(documents))
    response = chat(messages, system_prompt=system_prompt, **kwargs)

    result = _parse_json_response(response)
    if result and "topics" in result:
        logger.info("Extracted %d topics", len(result["topics"]))
        return result

    logger.warning("Topic extraction returned unparseable response")
    return {"topics": [], "overall_theme": "Analysis unavailable"}


# ---------------------------------------------------------------------------
# Sentiment analysis
# ---------------------------------------------------------------------------

def analyze_sentiment_trends(
    documents: list[dict], config: Optional[dict] = None
) -> dict:
    """Analyse sentiment patterns across *documents*.

    Returns:
        Dict with ``overall_sentiment``, ``sentiment_distribution``,
        ``sentiment_shifts``, ``key_positive_themes``, ``key_negative_themes``.
    """
    config = config or DEFAULT_CONFIG
    preview_chars = config.get("analysis", {}).get("preview_chars", 500)

    doc_summaries = [
        f"[{doc['filename']}]: {doc['content'][:preview_chars]}"
        for doc in documents[:15]
    ]
    combined = "\n\n".join(doc_summaries)

    system_prompt = (
        "You are a sentiment analysis expert. Analyze sentiment patterns across "
        "the provided documents. Respond ONLY with valid JSON:\n"
        '{"overall_sentiment": "positive|negative|neutral|mixed", '
        '"sentiment_distribution": {"positive": N, "negative": N, "neutral": N}, '
        '"sentiment_shifts": ["description of any notable shifts"], '
        '"key_positive_themes": ["theme1"], "key_negative_themes": ["theme1"]}'
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Analyze sentiment trends across these {len(documents)} "
                f"documents:\n\n{combined}"
            ),
        }
    ]

    kwargs = _model_kwargs(config)
    logger.info("Analyzing sentiment for %d documents", len(documents))
    response = chat(messages, system_prompt=system_prompt, **kwargs)

    result = _parse_json_response(response)
    if result and "overall_sentiment" in result:
        logger.info("Sentiment: %s", result["overall_sentiment"])
        return result

    logger.warning("Sentiment analysis returned unparseable response")
    return {
        "overall_sentiment": "neutral",
        "sentiment_distribution": {"positive": 0, "negative": 0, "neutral": 0},
        "sentiment_shifts": [],
        "key_positive_themes": [],
        "key_negative_themes": [],
    }


# ---------------------------------------------------------------------------
# Topic evolution tracking
# ---------------------------------------------------------------------------

def track_topic_evolution(
    documents: list[dict],
    previous_topics: Optional[dict] = None,
    config: Optional[dict] = None,
) -> dict:
    """Track how topics evolve over time across documents.

    Args:
        documents: Current set of documents.
        previous_topics: Topics dict from a prior analysis run (optional).
        config: Configuration dict.

    Returns:
        Dict with ``current_topics``, ``evolved``, ``new``, ``disappeared``,
        and ``evolution_summary``.
    """
    config = config or DEFAULT_CONFIG
    preview_chars = config.get("analysis", {}).get("preview_chars", 500)

    doc_summaries = [
        f"[{doc['filename']}]: {doc['content'][:preview_chars]}"
        for doc in documents[:20]
    ]
    combined = "\n\n".join(doc_summaries)

    prev_topics_json = json.dumps(previous_topics) if previous_topics else "none"

    system_prompt = (
        "You are a topic evolution analyst. Compare the current document set "
        "against previously identified topics and identify how topics have "
        "changed. Respond ONLY with valid JSON:\n"
        '{"current_topics": ["topic1"], '
        '"evolved": [{"topic": "name", "change": "description"}], '
        '"new": ["newly appeared topic"], '
        '"disappeared": ["topic no longer present"], '
        '"evolution_summary": "brief narrative"}'
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Track topic evolution.\n\nPrevious topics:\n{prev_topics_json}"
                f"\n\nCurrent documents:\n{combined}"
            ),
        }
    ]

    kwargs = _model_kwargs(config)
    logger.info("Tracking topic evolution across %d documents", len(documents))
    response = chat(messages, system_prompt=system_prompt, **kwargs)

    result = _parse_json_response(response)
    if result and "current_topics" in result:
        return result

    return {
        "current_topics": [],
        "evolved": [],
        "new": [],
        "disappeared": [],
        "evolution_summary": "Evolution analysis unavailable",
    }


# ---------------------------------------------------------------------------
# Sentiment-topic correlation
# ---------------------------------------------------------------------------

def correlate_sentiment_topics(topics: dict, sentiments: dict) -> dict:
    """Correlate sentiment data with extracted topics.

    Args:
        topics: Output of :func:`extract_topics`.
        sentiments: Output of :func:`analyze_sentiment_trends`.

    Returns:
        Dict with ``correlations`` list and ``summary``.
    """
    topic_list = topics.get("topics", [])
    positive_themes = sentiments.get("key_positive_themes", [])
    negative_themes = sentiments.get("key_negative_themes", [])
    overall = sentiments.get("overall_sentiment", "neutral")

    correlations: list[dict] = []
    for topic in topic_list:
        name = topic.get("name", "").lower()
        sentiment = "neutral"
        if any(name in t.lower() or t.lower() in name for t in positive_themes):
            sentiment = "positive"
        elif any(name in t.lower() or t.lower() in name for t in negative_themes):
            sentiment = "negative"

        correlations.append(
            {
                "topic": topic.get("name", "Unknown"),
                "frequency": topic.get("frequency", "low"),
                "trend": topic.get("trend", "stable"),
                "sentiment": sentiment,
            }
        )

    logger.info("Correlated %d topics with sentiment data", len(correlations))
    return {
        "correlations": correlations,
        "overall_sentiment": overall,
        "summary": (
            f"{len(correlations)} topics correlated; overall sentiment: {overall}"
        ),
    }


# ---------------------------------------------------------------------------
# Emerging topic detection
# ---------------------------------------------------------------------------

FREQUENCY_RANK = {"high": 3, "medium": 2, "low": 1}


def detect_emerging_topics(
    topics: dict, threshold: float = 0.7, config: Optional[dict] = None
) -> list[dict]:
    """Detect emerging or suddenly popular topics.

    A topic is considered *emerging* when its trend is ``"emerging"`` or
    ``"growing"`` and its frequency meets the configured minimum.

    Args:
        topics: Output of :func:`extract_topics`.
        threshold: Score threshold (0–1) for inclusion.
        config: Configuration dict.

    Returns:
        List of dicts with ``name``, ``score``, ``trend``, ``description``.
    """
    config = config or DEFAULT_CONFIG
    emg_cfg = config.get("emerging_detection", DEFAULT_CONFIG["emerging_detection"])
    min_freq = emg_cfg.get("min_frequency", "medium")
    min_freq_rank = FREQUENCY_RANK.get(min_freq, 2)

    emerging: list[dict] = []
    for topic in topics.get("topics", []):
        trend = topic.get("trend", "stable")
        freq = topic.get("frequency", "low")
        freq_rank = FREQUENCY_RANK.get(freq, 1)

        if trend not in ("emerging", "growing"):
            continue
        if freq_rank < min_freq_rank:
            continue

        # Simple heuristic score
        trend_score = 1.0 if trend == "emerging" else 0.8
        freq_score = freq_rank / 3.0
        score = round((trend_score * 0.6 + freq_score * 0.4), 2)

        if score >= threshold:
            emerging.append(
                {
                    "name": topic.get("name", "Unknown"),
                    "score": score,
                    "trend": trend,
                    "frequency": freq,
                    "description": topic.get("description", ""),
                }
            )

    emerging.sort(key=lambda t: t["score"], reverse=True)
    logger.info("Detected %d emerging topics (threshold=%.2f)", len(emerging), threshold)
    return emerging


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_trend_report(
    documents: list[dict],
    topics: dict,
    sentiments: dict,
    timeframe: str,
    config: Optional[dict] = None,
) -> str:
    """Generate a comprehensive trend report via LLM.

    Returns:
        Markdown-formatted report string.
    """
    config = config or DEFAULT_CONFIG
    topics_text = json.dumps(topics, indent=2)
    sentiments_text = json.dumps(sentiments, indent=2)

    system_prompt = (
        "You are a senior research analyst. Write a comprehensive trend analysis "
        "report. Be specific about emerging patterns, provide evidence from the "
        "data, and offer forward-looking insights. Format with markdown."
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Generate a trend analysis report for timeframe: {timeframe}\n\n"
                f"Documents analyzed: {len(documents)}\n\n"
                f"Extracted Topics:\n{topics_text}\n\n"
                f"Sentiment Analysis:\n{sentiments_text}\n\n"
                "Include:\n"
                "1. Executive Summary\n"
                "2. Emerging Topics & Trends\n"
                "3. Sentiment Analysis\n"
                "4. Key Insights\n"
                "5. Predictions & Outlook"
            ),
        }
    ]

    kwargs = _model_kwargs(config)
    kwargs["temperature"] = 0.4
    logger.info("Generating trend report for timeframe '%s'", timeframe)
    return chat(messages, system_prompt=system_prompt, **kwargs)


def generate_alert_report(emerging_topics: list[dict]) -> str:
    """Generate a short alert report for emerging topics.

    Args:
        emerging_topics: Output of :func:`detect_emerging_topics`.

    Returns:
        Markdown-formatted alert string.
    """
    if not emerging_topics:
        return "No emerging topics detected."

    lines = ["# 🚨 Emerging Topic Alerts\n"]
    for topic in emerging_topics:
        lines.append(
            f"## {topic['name']} (score: {topic['score']})\n"
            f"- **Trend:** {topic['trend']}\n"
            f"- **Frequency:** {topic.get('frequency', 'N/A')}\n"
            f"- {topic.get('description', '')}\n"
        )
    report = "\n".join(lines)
    logger.info("Generated alert report for %d topics", len(emerging_topics))
    return report


# ---------------------------------------------------------------------------
# Report scheduling
# ---------------------------------------------------------------------------

_DAY_MAP = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


def schedule_report(config: dict) -> dict:
    """Compute the next scheduled report run based on *config*.

    Returns:
        Dict with ``enabled``, ``frequency``, ``next_run``, ``day``, ``time``.
    """
    sched = config.get("schedule", DEFAULT_CONFIG["schedule"])
    enabled = sched.get("enabled", False)
    frequency = sched.get("frequency", "weekly")
    day = sched.get("day", "monday").lower()
    time_str = sched.get("time", "09:00")

    now = datetime.now()
    hour, minute = (int(p) for p in time_str.split(":"))

    if frequency == "daily":
        next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if next_run <= now:
            next_run += timedelta(days=1)
    elif frequency == "weekly":
        target_weekday = _DAY_MAP.get(day, 0)
        days_ahead = (target_weekday - now.weekday()) % 7
        next_run = (now + timedelta(days=days_ahead)).replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )
        if next_run <= now:
            next_run += timedelta(weeks=1)
    elif frequency == "monthly":
        next_run = now.replace(day=1, hour=hour, minute=minute, second=0, microsecond=0)
        if next_run <= now:
            month = now.month % 12 + 1
            year = now.year + (1 if month == 1 else 0)
            next_run = next_run.replace(year=year, month=month)
    else:
        next_run = now

    result = {
        "enabled": enabled,
        "frequency": frequency,
        "day": day,
        "time": time_str,
        "next_run": next_run.isoformat(),
    }
    logger.info("Schedule: next_run=%s enabled=%s", result["next_run"], enabled)
    return result


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------

def compute_analytics(
    documents: list[dict], topics: dict, sentiments: dict
) -> dict:
    """Compute summary analytics from analysis results.

    Returns:
        Dict with document stats, topic stats, sentiment stats, and
        correlation data.
    """
    total_size = sum(d.get("size", 0) for d in documents)
    topic_list = topics.get("topics", [])
    dist = sentiments.get("sentiment_distribution", {})

    correlations = correlate_sentiment_topics(topics, sentiments)

    analytics = {
        "documents": {
            "count": len(documents),
            "total_size": total_size,
            "avg_size": round(total_size / len(documents)) if documents else 0,
        },
        "topics": {
            "count": len(topic_list),
            "emerging": sum(
                1 for t in topic_list if t.get("trend") == "emerging"
            ),
            "growing": sum(
                1 for t in topic_list if t.get("trend") == "growing"
            ),
            "stable": sum(
                1 for t in topic_list if t.get("trend") == "stable"
            ),
            "declining": sum(
                1 for t in topic_list if t.get("trend") == "declining"
            ),
        },
        "sentiment": {
            "overall": sentiments.get("overall_sentiment", "neutral"),
            "positive": dist.get("positive", 0),
            "negative": dist.get("negative", 0),
            "neutral": dist.get("neutral", 0),
        },
        "correlations": correlations,
    }
    logger.info("Computed analytics for %d documents", len(documents))
    return analytics
