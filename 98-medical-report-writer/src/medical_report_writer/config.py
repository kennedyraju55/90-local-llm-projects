"""
Medical Report Writer - Configuration Module

Loads settings from config.yaml with sensible defaults.
"""

import os
import logging
from typing import Any

logger = logging.getLogger("medical_report_writer.config")


def load_config() -> dict[str, Any]:
    """Load configuration from config.yaml or use defaults.

    Returns:
        dict with configuration values.
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    defaults: dict[str, Any] = {
        "model": "gemma4",
        "temperature": 0.3,
        "max_tokens": 3072,
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


def setup_logging(level: str = "INFO") -> None:
    """Configure logging for the medical report writer.

    Args:
        level: Logging level string (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
