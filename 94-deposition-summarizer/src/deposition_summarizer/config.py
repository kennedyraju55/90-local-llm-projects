"""Configuration management for Deposition Summarizer."""

import os
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)


@dataclass
class LLMConfig:
    """LLM configuration settings."""
    model: str = "gemma4:latest"
    temperature: float = 0.3
    max_tokens: int = 4096
    ollama_host: str = "http://localhost:11434"


@dataclass
class AppConfig:
    """Application configuration settings."""
    name: str = "Deposition Summarizer"
    version: str = "1.0.0"
    highlight_threshold: str = "medium"
    max_transcript_length: int = 50000
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    llm: LLMConfig = field(default_factory=LLMConfig)


DEFAULT_CONFIG: dict[str, Any] = {
    "app": {
        "name": "Deposition Summarizer",
        "version": "1.0.0",
    },
    "llm": {
        "model": "gemma4:latest",
        "temperature": 0.3,
        "max_tokens": 4096,
        "ollama_host": "http://localhost:11434",
    },
    "analysis": {
        "highlight_threshold": "medium",
        "max_transcript_length": 50000,
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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
    config = _deep_copy(DEFAULT_CONFIG)

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
    if env_model := os.environ.get("DEPOSITION_SUMMARIZER_MODEL"):
        config["llm"]["model"] = env_model
    if env_temp := os.environ.get("DEPOSITION_SUMMARIZER_TEMPERATURE"):
        config["llm"]["temperature"] = float(env_temp)
    if env_host := os.environ.get("OLLAMA_HOST"):
        config["llm"]["ollama_host"] = env_host

    return config


def _deep_copy(d: dict) -> dict:
    """Deep copy a nested dict."""
    result = {}
    for k, v in d.items():
        if isinstance(v, dict):
            result[k] = _deep_copy(v)
        elif isinstance(v, list):
            result[k] = v.copy()
        else:
            result[k] = v
    return result


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override dict into base dict."""
    merged = base.copy()
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
