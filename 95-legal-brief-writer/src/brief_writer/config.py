"""Configuration management for Legal Brief Writer."""

import os
import yaml
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LLMConfig:
    """LLM configuration."""
    model: str = "gemma4:latest"
    temperature: float = 0.4
    max_tokens: int = 8192
    ollama_host: str = "http://localhost:11434"


@dataclass
class WritingConfig:
    """Writing configuration."""
    default_brief_type: str = "memorandum_of_law"
    max_word_count: int = 15000


@dataclass
class LoggingConfig:
    """Logging configuration."""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@dataclass
class AppConfig:
    """Application configuration."""
    name: str = "Legal Brief Writer"
    version: str = "1.0.0"
    llm: LLMConfig = field(default_factory=LLMConfig)
    writing: WritingConfig = field(default_factory=WritingConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def load_config(config_path: Optional[str] = None) -> AppConfig:
    """Load configuration from YAML file.

    Args:
        config_path: Path to config file. Defaults to config.yaml in project root.

    Returns:
        AppConfig instance with loaded settings.
    """
    if config_path is None:
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "config.yaml"
        )

    config = AppConfig()

    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            data = yaml.safe_load(f) or {}

        app_data = data.get("app", {})
        if app_data:
            config.name = app_data.get("name", config.name)
            config.version = app_data.get("version", config.version)

        llm_data = data.get("llm", {})
        if llm_data:
            config.llm.model = llm_data.get("model", config.llm.model)
            config.llm.temperature = llm_data.get("temperature", config.llm.temperature)
            config.llm.max_tokens = llm_data.get("max_tokens", config.llm.max_tokens)
            config.llm.ollama_host = llm_data.get("ollama_host", config.llm.ollama_host)

        writing_data = data.get("writing", {})
        if writing_data:
            config.writing.default_brief_type = writing_data.get(
                "default_brief_type", config.writing.default_brief_type
            )
            config.writing.max_word_count = writing_data.get(
                "max_word_count", config.writing.max_word_count
            )

        logging_data = data.get("logging", {})
        if logging_data:
            config.logging.level = logging_data.get("level", config.logging.level)
            config.logging.format = logging_data.get("format", config.logging.format)

    # Environment variable overrides
    config.llm.model = os.environ.get("LLM_MODEL", config.llm.model)
    config.llm.ollama_host = os.environ.get("OLLAMA_HOST", config.llm.ollama_host)
    config.llm.temperature = float(os.environ.get("LLM_TEMPERATURE", str(config.llm.temperature)))
    config.llm.max_tokens = int(os.environ.get("LLM_MAX_TOKENS", str(config.llm.max_tokens)))

    return config
