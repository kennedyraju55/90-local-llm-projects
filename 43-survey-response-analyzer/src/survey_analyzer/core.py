"""Core logic for Survey Response Analyzer."""

import os
import sys
import csv
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


def load_survey_data(file_path: str) -> list[dict]:
    """Load survey responses from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            raise ValueError("CSV file is empty.")
        logger.info("Loaded %d survey responses from %s", len(rows), file_path)
        return rows
    except Exception as e:
        if isinstance(e, (FileNotFoundError, ValueError)):
            raise
        raise ValueError(f"Error reading CSV: {e}")


def identify_text_columns(data: list[dict]) -> list[str]:
    """Identify columns likely containing free-text responses."""
    text_cols = []
    for col in data[0].keys():
        sample_values = [row.get(col, "") for row in data[:10]]
        avg_len = sum(len(str(v)) for v in sample_values) / max(len(sample_values), 1)
        if avg_len > 20:
            text_cols.append(col)
    return text_cols if text_cols else list(data[0].keys())


def identify_demographic_columns(data: list[dict]) -> list[str]:
    """Identify columns that are likely demographic/categorical."""
    demo_cols = []
    demo_keywords = ["age", "gender", "location", "department", "role", "region", "country", "group"]
    for col in data[0].keys():
        col_lower = col.lower()
        if any(kw in col_lower for kw in demo_keywords):
            demo_cols.append(col)
            continue
        nunique = len(set(row.get(col, "") for row in data))
        ratio = nunique / len(data) if len(data) > 0 else 0
        if ratio < 0.1 and nunique < 15:
            demo_cols.append(col)
    return demo_cols


def extract_themes(responses: list[str]) -> dict:
    """Extract major themes from survey responses."""
    chat, _ = get_llm_client()
    combined = "\n".join(f"- {r}" for r in responses[:50])

    system_prompt = (
        "You are a survey analysis expert. Analyze the survey responses and identify "
        "the major themes. Respond ONLY with valid JSON:\n"
        '{"themes": [{"name": "theme name", "count": estimated_count, '
        '"description": "brief description", "sentiment": "positive|negative|mixed", '
        '"representative_quotes": ["quote1"]}], '
        '"total_responses": N}'
    )

    messages = [{"role": "user", "content": f"Analyze these {len(responses)} survey responses:\n\n{combined}"}]
    response = chat(messages, system_prompt=system_prompt, temperature=0.3, max_tokens=3000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {"themes": [], "total_responses": len(responses)}


def cluster_themes(themes: dict) -> list[dict]:
    """Group related themes into clusters."""
    chat, _ = get_llm_client()
    if not themes.get("themes"):
        return []

    themes_text = json.dumps(themes["themes"], indent=2)
    system_prompt = (
        "You are an expert at thematic analysis. Group the given themes into higher-level clusters. "
        "Respond ONLY with valid JSON:\n"
        '{"clusters": [{"cluster_name": "name", "themes": ["theme1", "theme2"], '
        '"overall_sentiment": "positive|negative|mixed", "priority": "high|medium|low"}]}'
    )

    messages = [{"role": "user", "content": f"Group these themes into clusters:\n\n{themes_text}"}]
    response = chat(messages, system_prompt=system_prompt, temperature=0.3, max_tokens=2000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(response[start:end])
            return result.get("clusters", [])
    except (json.JSONDecodeError, ValueError):
        pass
    return []


def compute_demographic_crosstabs(data: list[dict], text_col: str, demo_col: str,
                                   themes: dict) -> dict:
    """Compute cross-tabulation of themes by demographic group."""
    groups = {}
    for row in data:
        group = row.get(demo_col, "Unknown")
        response = str(row.get(text_col, "")).strip()
        if response:
            if group not in groups:
                groups[group] = []
            groups[group].append(response)

    crosstab = {}
    for group, responses in groups.items():
        crosstab[group] = {
            "count": len(responses),
            "avg_length": round(sum(len(r) for r in responses) / max(len(responses), 1), 1),
        }

    return {"demographic_column": demo_col, "groups": crosstab}


def highlight_verbatims(responses: list[str], themes: dict) -> list[dict]:
    """Identify and highlight notable verbatim responses."""
    chat, _ = get_llm_client()
    combined = "\n".join(f"- {r}" for r in responses[:30])
    themes_text = json.dumps([t["name"] for t in themes.get("themes", [])], indent=2)

    system_prompt = (
        "You are an expert at qualitative analysis. Identify the most impactful and "
        "representative verbatim responses. Respond ONLY with valid JSON:\n"
        '{"verbatims": [{"text": "quote", "theme": "theme name", "impact": "high|medium", '
        '"reason": "why this is notable"}]}'
    )

    messages = [{"role": "user", "content": (
        f"Themes: {themes_text}\n\nResponses:\n{combined}\n\n"
        "Identify 5-8 most impactful verbatim quotes."
    )}]
    response = chat(messages, system_prompt=system_prompt, temperature=0.3, max_tokens=2000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(response[start:end])
            return result.get("verbatims", [])
    except (json.JSONDecodeError, ValueError):
        pass
    return []


def generate_recommendations(responses: list[str], themes: dict) -> list[dict]:
    """Generate actionable recommendations based on analysis."""
    chat, _ = get_llm_client()
    themes_text = json.dumps(themes.get("themes", []), indent=2)

    system_prompt = (
        "You are a strategic consultant. Based on survey analysis, generate actionable "
        "recommendations. Respond ONLY with valid JSON:\n"
        '{"recommendations": [{"title": "title", "description": "details", '
        '"priority": "high|medium|low", "effort": "low|medium|high", '
        '"expected_impact": "description of impact"}]}'
    )

    messages = [{"role": "user", "content": (
        f"Based on {len(responses)} survey responses with these themes:\n\n"
        f"{themes_text}\n\nGenerate 5-7 actionable recommendations."
    )}]
    response = chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=3000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(response[start:end])
            return result.get("recommendations", [])
    except (json.JSONDecodeError, ValueError):
        pass
    return []


def generate_insights(responses: list[str], themes: dict) -> str:
    """Generate detailed insights from the survey data."""
    chat, _ = get_llm_client()
    combined = "\n".join(f"- {r}" for r in responses[:30])
    themes_text = json.dumps(themes.get("themes", []), indent=2)

    system_prompt = (
        "You are a survey analysis expert. Generate a detailed insights report "
        "based on survey responses and identified themes. Include actionable "
        "recommendations. Format with markdown headings and bullet points."
    )

    messages = [{"role": "user", "content": (
        f"Survey Responses Sample:\n{combined}\n\n"
        f"Identified Themes:\n{themes_text}\n\n"
        "Generate a comprehensive insights report with:\n"
        "1. Executive Summary\n"
        "2. Key Findings\n"
        "3. Theme Analysis\n"
        "4. Actionable Recommendations"
    )}]

    return chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=4000)
