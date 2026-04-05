"""Configuration management for Resume Analyzer."""

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
    "ats": {
        "keyword_weight": 0.4,
        "experience_weight": 0.3,
        "education_weight": 0.15,
        "formatting_weight": 0.15,
    },
    "output": {
        "default_format": "rich",
    },
}


def find_config_file() -> Path | None:
    candidates = [
        Path(__file__).parent.parent.parent / "config.yaml",
        Path.cwd() / "config.yaml",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def load_config(config_path: str | None = None) -> dict[str, Any]:
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

    if env_model := os.environ.get("RESUME_ANALYZER_MODEL"):
        config["llm"]["model"] = env_model
    if env_temp := os.environ.get("RESUME_ANALYZER_TEMPERATURE"):
        config["llm"]["temperature"] = float(env_temp)
    return config


def _deep_merge(base: dict, override: dict) -> dict:
    merged = base.copy()
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
