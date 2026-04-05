"""Configuration management for Legal Document Summarizer."""

import os
import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "llm": {
        "model": "gemma4",
        "temperature": 0.3,
        "max_tokens": 4096,
    },
    "processing": {
        "max_document_chars": 12000,
        "supported_formats": [".txt", ".text", ".md", ".pdf"],
    },
    "risk_scoring": {
        "high_risk_keywords": [
            "indemnification", "unlimited liability", "non-compete",
            "automatic renewal", "liquidated damages", "waiver",
            "sole discretion", "irrevocable", "perpetual license",
        ],
        "medium_risk_keywords": [
            "termination for convenience", "assignment", "governing law",
            "force majeure", "limitation of liability", "confidentiality",
        ],
    },
    "output": {
        "default_format": "bullet",
        "available_formats": ["bullet", "narrative", "detailed"],
    },
}


def find_config_file() -> Path | None:
    """Locate config.yaml in the project directory."""
    candidates = [
        Path(__file__).parent.parent.parent / "config.yaml",
        Path.cwd() / "config.yaml",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def load_config(config_path: str | None = None) -> dict[str, Any]:
    """Load configuration from YAML file, falling back to defaults.

    Args:
        config_path: Optional explicit path to config.yaml.

    Returns:
        Merged configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()

    path = Path(config_path) if config_path else find_config_file()
    if path and path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                user_config = yaml.safe_load(f) or {}
            config = _deep_merge(config, user_config)
            logger.info("Loaded config from %s", path)
        except Exception as e:
            logger.warning("Failed to load config from %s: %s", path, e)
    else:
        logger.debug("No config file found, using defaults.")

    # Environment variable overrides
    if env_model := os.environ.get("LEGAL_SUMMARIZER_MODEL"):
        config["llm"]["model"] = env_model
    if env_temp := os.environ.get("LEGAL_SUMMARIZER_TEMPERATURE"):
        config["llm"]["temperature"] = float(env_temp)

    return config


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override dict into base dict."""
    merged = base.copy()
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
