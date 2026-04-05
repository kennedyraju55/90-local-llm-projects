"""Configuration management for Invoice Extractor."""

import os
import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "llm": {
        "model": "gemma4",
        "temperature": 0.1,
        "max_tokens": 4096,
    },
    "processing": {
        "batch_size": 10,
        "duplicate_threshold": 0.9,
    },
    "categories": [
        "Office Supplies", "Software", "Hardware", "Consulting",
        "Travel", "Utilities", "Marketing", "Other",
    ],
    "output": {
        "default_format": "json",
        "csv_delimiter": ",",
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
        except Exception as e:
            logger.warning("Failed to load config: %s", e)

    if env_model := os.environ.get("INVOICE_EXTRACTOR_MODEL"):
        config["llm"]["model"] = env_model
    if env_temp := os.environ.get("INVOICE_EXTRACTOR_TEMPERATURE"):
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
