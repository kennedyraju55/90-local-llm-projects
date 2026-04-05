"""Core logic for Competitor Analysis Tool."""

import os
import sys
import json
import logging
from typing import Any, Dict, List, Optional, Tuple, Union

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


def generate_swot(company: str, competitors: list[str], industry: str) -> dict:
    """Generate SWOT analysis for the company vs competitors."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a strategic business analyst. Generate a comprehensive SWOT analysis. "
        "Respond ONLY with valid JSON in this exact format:\n"
        '{"strengths": ["s1", "s2", "s3"], "weaknesses": ["w1", "w2", "w3"], '
        '"opportunities": ["o1", "o2", "o3"], "threats": ["t1", "t2", "t3"]}'
    )

    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Company: {company}\n"
        f"Competitors: {competitors_text}\n"
        f"Industry: {industry}\n\n"
        "Generate a detailed SWOT analysis for the company considering the competitive landscape."
    )}]

    response = chat(messages, system_prompt=system_prompt, temperature=0.4)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {
        "strengths": ["Analysis unavailable"],
        "weaknesses": ["Analysis unavailable"],
        "opportunities": ["Analysis unavailable"],
        "threats": ["Analysis unavailable"],
    }


def generate_feature_matrix(company: str, competitors: list[str], industry: str) -> dict:
    """Generate a feature comparison matrix."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a product analyst. Create a feature comparison matrix. "
        "Respond ONLY with valid JSON:\n"
        '{"features": ["feat1", "feat2", "feat3"], '
        '"matrix": {"Company1": {"feat1": "yes|no|partial", ...}, ...}, '
        '"summary": "brief comparison summary"}'
    )

    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Create a feature comparison matrix for {company} vs {competitors_text} "
        f"in the {industry} industry. Include 8-10 key features."
    )}]

    response = chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=3000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {"features": [], "matrix": {}, "summary": "Feature comparison unavailable"}


def generate_pricing_comparison(company: str, competitors: list[str], industry: str) -> dict:
    """Generate pricing comparison analysis."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a pricing strategist. Compare pricing strategies. "
        "Respond ONLY with valid JSON:\n"
        '{"companies": [{"name": "company", "pricing_model": "description", '
        '"price_range": "range", "value_proposition": "description", '
        '"tier": "budget|mid-range|premium"}], '
        '"recommendation": "pricing strategy recommendation"}'
    )

    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Compare pricing strategies for {company} vs {competitors_text} in {industry}."
    )}]

    response = chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=2000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {"companies": [], "recommendation": "Pricing analysis unavailable"}


def generate_market_positioning(company: str, competitors: list[str], industry: str) -> dict:
    """Generate market positioning analysis."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a market positioning expert. Analyze market positions. "
        "Respond ONLY with valid JSON:\n"
        '{"positions": [{"company": "name", "x_axis": 1-10, "y_axis": 1-10, '
        '"x_label": "Price (Low→High)", "y_label": "Quality (Low→High)", '
        '"quadrant": "description"}], '
        '"market_gaps": ["gap1", "gap2"], '
        '"positioning_summary": "summary"}'
    )

    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Analyze market positioning for {company} vs {competitors_text} in {industry}. "
        "Map on Price vs Quality axes (1-10 scale)."
    )}]

    response = chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=2000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])
    except (json.JSONDecodeError, ValueError):
        pass

    return {"positions": [], "market_gaps": [], "positioning_summary": "Analysis unavailable"}


def generate_comparison(company: str, competitors: list[str], industry: str) -> str:
    """Generate a competitive comparison analysis report."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a market research analyst. Create a detailed competitive comparison "
        "report. Use markdown formatting with tables where appropriate. "
        "Compare features, pricing strategy, market position, and differentiation."
    )

    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Compare {company} against these competitors in the {industry} industry: "
        f"{competitors_text}\n\n"
        "Provide analysis on:\n"
        "1. Feature Comparison\n"
        "2. Pricing & Value Proposition\n"
        "3. Market Position & Share\n"
        "4. Key Differentiators\n"
        "5. Strategic Recommendations"
    )}]

    return chat(messages, system_prompt=system_prompt, temperature=0.5, max_tokens=4000)


def generate_action_items(company: str, competitors: list[str], industry: str,
                           swot: dict, features: dict = None) -> list[dict]:
    """Generate prioritized action items."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a strategic consultant. Generate prioritized action items. "
        "Respond ONLY with valid JSON:\n"
        '{"action_items": [{"title": "title", "description": "details", '
        '"priority": "critical|high|medium|low", "timeline": "immediate|short-term|long-term", '
        '"category": "product|marketing|operations|strategy", '
        '"expected_outcome": "description"}]}'
    )

    swot_text = json.dumps(swot, indent=2)
    messages = [{"role": "user", "content": (
        f"Company: {company}\nIndustry: {industry}\n\n"
        f"SWOT Analysis:\n{swot_text}\n\n"
        "Generate 5-8 prioritized strategic action items."
    )}]

    response = chat(messages, system_prompt=system_prompt, temperature=0.5, max_tokens=3000)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(response[start:end])
            return result.get("action_items", [])
    except (json.JSONDecodeError, ValueError):
        pass
    return []


def generate_recommendations(company: str, competitors: list[str], industry: str, swot: dict) -> str:
    """Generate strategic recommendations based on the analysis."""
    chat, _ = get_llm_client()
    system_prompt = (
        "You are a strategic business consultant. Based on the SWOT analysis provided, "
        "generate actionable strategic recommendations. Use markdown formatting."
    )

    swot_text = json.dumps(swot, indent=2)
    competitors_text = ", ".join(competitors)
    messages = [{"role": "user", "content": (
        f"Company: {company}\n"
        f"Competitors: {competitors_text}\n"
        f"Industry: {industry}\n\n"
        f"SWOT Analysis:\n{swot_text}\n\n"
        "Generate top 5 strategic recommendations with rationale and priority level."
    )}]

    return chat(messages, system_prompt=system_prompt, temperature=0.5, max_tokens=3000)
