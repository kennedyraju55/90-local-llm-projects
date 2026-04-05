"""
Patient Intake Summarizer - Configuration Module

Loads settings from config.yaml with sensible defaults.
"""

import os
import logging
from typing import Any


logger = logging.getLogger("patient_intake_summarizer.config")


def load_config() -> dict[str, Any]:
    """Load configuration from config.yaml or use defaults."""
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    defaults: dict[str, Any] = {
        "model": "gemma4",
        "temperature": 0.3,
        "max_tokens": 2048,
        "log_level": "INFO",
        "ollama_url": "http://localhost:11434",
    }
    try:
        import yaml
        with open(config_path, 'r') as f:
            user_config = yaml.safe_load(f) or {}
        defaults.update(user_config)
    except (ImportError, FileNotFoundError):
        pass
    return defaults
