"""
Configuration loader for Lab Results Interpreter.
Reads settings from config.yaml with sensible defaults.
"""

import os
import yaml
from typing import Any, Dict


DEFAULT_CONFIG = {
    "model": "gemma4",
    "temperature": 0.3,
    "max_tokens": 2048,
    "log_level": "INFO",
    "ollama_url": "http://localhost:11434",
    "ui": {
        "theme": "medical",
        "show_disclaimer": True,
        "show_history": True,
    },
}


def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration from config.yaml or environment variables.

    Priority: env vars > config.yaml > defaults.

    Args:
        config_path: Optional path to config.yaml file.

    Returns:
        Merged configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()

    if config_path is None:
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "config.yaml",
        )

    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            file_config = yaml.safe_load(f) or {}
            config.update(file_config)

    # Environment variable overrides
    env_mappings = {
        "OLLAMA_MODEL": "model",
        "OLLAMA_BASE_URL": "ollama_url",
        "OLLAMA_HOST": "ollama_url",
        "LOG_LEVEL": "log_level",
    }
    for env_var, config_key in env_mappings.items():
        val = os.environ.get(env_var)
        if val:
            config[config_key] = val

    return config
