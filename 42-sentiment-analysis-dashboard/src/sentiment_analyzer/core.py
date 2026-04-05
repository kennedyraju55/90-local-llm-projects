"""Core logic for Sentiment Analysis Dashboard."""

import os
import sys
import json
import logging
from typing import Any, Dict, List, Optional, Tuple, Union
from collections import Counter

import yaml

logger = logging.getLogger(__name__)

_config: Optional[dict] = None


def load_config(config_path: str = None) -> dict:
    """Load configuration from config.yaml."""
    global _config
    if _config is not None and config_path is None:
        return _config
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")
    try:
        with open(config_path, "r") as f:
            _config = yaml.safe_load(f) or {}
    except FileNotFoundError:
        logger.warning("Config file not found at %s, using defaults", config_path)
        _config = {}
    return _config


def get_llm_client() -> Tuple[Any, ...]:
    """Get LLM client with proper path setup."""
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    parent_dir = os.path.dirname(project_root)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    from common.llm_client import chat, check_ollama_running
    return chat, check_ollama_running


def read_text_file(file_path: str) -> list[str]:
    """Read a text file and return non-empty lines."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        if not lines:
            raise ValueError("File is empty.")
        return lines
    except UnicodeDecodeError as e:
        raise ValueError(f"Cannot read file (encoding error): {e}")


def read_batch_files(file_paths: list[str]) -> dict[str, list[str]]:
    """Read multiple text files for batch processing."""
    results = {}
    for fp in file_paths:
        try:
            results[fp] = read_text_file(fp)
            logger.info("Loaded %d entries from %s", len(results[fp]), fp)
        except (FileNotFoundError, ValueError) as e:
            logger.warning("Skipping %s: %s", fp, e)
            results[fp] = []
    return results


def analyze_sentiment(text: str) -> dict:
    """Analyze sentiment of a single text entry."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a sentiment analysis expert. Analyze the sentiment of the given text. "
        "Respond ONLY with valid JSON in this exact format:\n"
        '{"sentiment": "positive|negative|neutral", "confidence": 0.0-1.0, '
        '"key_phrases": ["phrase1", "phrase2"], "summary": "brief explanation"}\n'
        "Do not include any other text outside the JSON."
    )

    messages = [{"role": "user", "content": f"Analyze the sentiment of this text:\n\n{text}"}]
    response = chat(messages, system_prompt=system_prompt, temperature=0.2)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {
        "sentiment": "neutral",
        "confidence": 0.5,
        "key_phrases": [],
        "summary": response[:200],
    }


def batch_analyze(texts: list[str], source: str = "default") -> list[dict]:
    """Analyze sentiment for a batch of texts."""
    results = []
    for i, text in enumerate(texts):
        logger.debug("Analyzing entry %d/%d from %s", i + 1, len(texts), source)
        result = analyze_sentiment(text)
        result["source"] = source
        result["index"] = i
        results.append(result)
    return results


def compute_sentiment_distribution(results: list[dict]) -> dict:
    """Compute sentiment distribution statistics."""
    total = len(results)
    if total == 0:
        return {"total": 0, "positive": 0, "negative": 0, "neutral": 0}

    counts = Counter(r.get("sentiment", "neutral").lower() for r in results)
    total_confidence = sum(r.get("confidence", 0.5) for r in results)

    return {
        "total": total,
        "positive": counts.get("positive", 0),
        "negative": counts.get("negative", 0),
        "neutral": counts.get("neutral", 0),
        "positive_pct": round(counts.get("positive", 0) / total * 100, 1),
        "negative_pct": round(counts.get("negative", 0) / total * 100, 1),
        "neutral_pct": round(counts.get("neutral", 0) / total * 100, 1),
        "avg_confidence": round(total_confidence / total, 3),
    }


def compute_trend_over_time(results: list[dict], window: int = 5) -> list[dict]:
    """Compute sentiment trend using a sliding window."""
    if len(results) < window:
        window = max(1, len(results))

    trend = []
    for i in range(0, len(results), window):
        chunk = results[i:i + window]
        dist = compute_sentiment_distribution(chunk)
        trend.append({
            "window_start": i,
            "window_end": min(i + window, len(results)),
            "positive_pct": dist["positive_pct"],
            "negative_pct": dist["negative_pct"],
            "neutral_pct": dist["neutral_pct"],
            "avg_confidence": dist["avg_confidence"],
        })
    return trend


def extract_word_cloud_data(results: list[dict]) -> dict[str, int]:
    """Extract word frequency data from key phrases for word cloud."""
    word_freq = Counter()
    for r in results:
        for phrase in r.get("key_phrases", []):
            for word in phrase.lower().split():
                if len(word) > 2:
                    word_freq[word] += 1
    return dict(word_freq.most_common(50))


def compare_sources(source_results: dict[str, list[dict]]) -> dict:
    """Compare sentiment across different sources."""
    comparison = {}
    for source, results in source_results.items():
        comparison[source] = compute_sentiment_distribution(results)
    return comparison


def export_report(results: list[dict], texts: list[str], output_path: str) -> str:
    """Export sentiment analysis report to JSON."""
    distribution = compute_sentiment_distribution(results)
    trend = compute_trend_over_time(results)
    word_cloud = extract_word_cloud_data(results)

    report = {
        "summary": distribution,
        "trend": trend,
        "word_cloud_data": word_cloud,
        "detailed_results": [
            {"text": text, **result}
            for text, result in zip(texts, results)
        ],
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2, default=str)

    logger.info("Report exported to %s", output_path)
    return output_path
