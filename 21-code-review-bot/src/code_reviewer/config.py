"""Configuration management for Code Reviewer."""

import os
import yaml
import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


@dataclass
class ReviewConfig:
    """Configuration for code review settings."""
    ollama_base_url: str = "http://localhost:11434"
    model: str = "gemma4"
    temperature: float = 0.3
    max_tokens: int = 4096
    severity_levels: list = field(default_factory=lambda: ["HIGH", "MEDIUM", "LOW"])
    categories: list = field(default_factory=lambda: [
        "BUG", "STYLE", "SECURITY", "PERFORMANCE", "BEST_PRACTICE"
    ])
    max_file_size_kb: int = 500
    output_format: str = "markdown"
    log_level: str = "INFO"


def load_config(config_path: Optional[str] = None) -> ReviewConfig:
    """Load configuration from YAML file with environment variable overrides."""
    path = config_path or os.environ.get("CODE_REVIEWER_CONFIG", DEFAULT_CONFIG_PATH)
    config = ReviewConfig()

    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            for key, value in data.items():
                if hasattr(config, key):
                    setattr(config, key, value)
            logger.info("Configuration loaded from %s", path)
        except Exception as e:
            logger.warning("Failed to load config from %s: %s", path, e)

    # Environment variable overrides
    if url := os.environ.get("OLLAMA_BASE_URL"):
        config.ollama_base_url = url
    if model := os.environ.get("OLLAMA_MODEL"):
        config.model = model
    if level := os.environ.get("LOG_LEVEL"):
        config.log_level = level

    return config


def setup_logging(config: ReviewConfig) -> None:
    """Configure logging based on config."""
    logging.basicConfig(
        level=getattr(logging, config.log_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
