"""Configuration management for Regex Gen."""

import os
import yaml
import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")

REGEX_FLAVORS = ["python", "javascript", "pcre", "posix", "java", "dotnet", "go", "rust"]

PATTERN_LIBRARY = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url": r"https?://[^\s/$.?#].[^\s]*",
    "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "phone_us": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "date_iso": r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])",
    "hex_color": r"#(?:[0-9a-fA-F]{3}){1,2}\b",
    "uuid": r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "credit_card": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
    "zip_us": r"\b\d{5}(?:-\d{4})?\b",
    "username": r"^[a-zA-Z0-9_]{3,20}$",
    "password_strong": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
}


@dataclass
class RegexConfig:
    """Configuration for regex generation."""
    ollama_base_url: str = "http://localhost:11434"
    model: str = "gemma4"
    temperature: float = 0.3
    max_tokens: int = 2048
    default_flavor: str = "python"
    log_level: str = "INFO"


def load_config(config_path: Optional[str] = None) -> RegexConfig:
    """Load configuration from YAML file with environment variable overrides."""
    path = config_path or os.environ.get("REGEX_GEN_CONFIG", DEFAULT_CONFIG_PATH)
    config = RegexConfig()

    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            for key, value in data.items():
                if hasattr(config, key):
                    setattr(config, key, value)
        except Exception as e:
            logger.warning("Failed to load config: %s", e)

    if url := os.environ.get("OLLAMA_BASE_URL"):
        config.ollama_base_url = url
    if model := os.environ.get("OLLAMA_MODEL"):
        config.model = model
    if level := os.environ.get("LOG_LEVEL"):
        config.log_level = level

    return config


def setup_logging(config: RegexConfig) -> None:
    """Configure logging."""
    logging.basicConfig(
        level=getattr(logging, config.log_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
