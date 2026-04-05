"""Configuration module for Court Filing Generator."""

import os
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class LLMConfig:
    """LLM configuration settings."""
    model: str = "gemma4:latest"
    temperature: float = 0.3
    max_tokens: int = 4096
    ollama_host: str = "http://localhost:11434"


@dataclass
class FilingConfig:
    """Filing-specific configuration."""
    default_jurisdiction: str = "federal"
    default_court: str = "United States District Court"


@dataclass
class LoggingConfig:
    """Logging configuration."""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@dataclass
class AppConfig:
    """Application configuration."""
    name: str = "Court Filing Generator"
    version: str = "1.0.0"
    llm: LLMConfig = field(default_factory=LLMConfig)
    filing: FilingConfig = field(default_factory=FilingConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def load_config(config_path: Optional[str] = None) -> AppConfig:
    """
    Load configuration from YAML file with environment variable overrides.

    Args:
        config_path: Path to config.yaml. If None, looks in project root.

    Returns:
        AppConfig instance with merged settings.
    """
    config = AppConfig()

    # Determine config file path
    if config_path is None:
        project_root = Path(__file__).parent.parent.parent
        config_path = str(project_root / "config.yaml")

    # Load YAML config if it exists
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}

        # App settings
        app_cfg = raw.get("app", {})
        config.name = app_cfg.get("name", config.name)
        config.version = app_cfg.get("version", config.version)

        # LLM settings
        llm_cfg = raw.get("llm", {})
        config.llm.model = llm_cfg.get("model", config.llm.model)
        config.llm.temperature = float(llm_cfg.get("temperature", config.llm.temperature))
        config.llm.max_tokens = int(llm_cfg.get("max_tokens", config.llm.max_tokens))
        config.llm.ollama_host = llm_cfg.get("ollama_host", config.llm.ollama_host)

        # Filing settings
        filing_cfg = raw.get("filing", {})
        config.filing.default_jurisdiction = filing_cfg.get(
            "default_jurisdiction", config.filing.default_jurisdiction
        )
        config.filing.default_court = filing_cfg.get(
            "default_court", config.filing.default_court
        )

        # Logging settings
        log_cfg = raw.get("logging", {})
        config.logging.level = log_cfg.get("level", config.logging.level)
        config.logging.format = log_cfg.get("format", config.logging.format)

    # Environment variable overrides
    if os.environ.get("OLLAMA_HOST"):
        config.llm.ollama_host = os.environ["OLLAMA_HOST"]
    if os.environ.get("OLLAMA_MODEL"):
        config.llm.model = os.environ["OLLAMA_MODEL"]
    if os.environ.get("LOG_LEVEL"):
        config.logging.level = os.environ["LOG_LEVEL"]
    if os.environ.get("DEFAULT_JURISDICTION"):
        config.filing.default_jurisdiction = os.environ["DEFAULT_JURISDICTION"]
    if os.environ.get("DEFAULT_COURT"):
        config.filing.default_court = os.environ["DEFAULT_COURT"]

    return config
