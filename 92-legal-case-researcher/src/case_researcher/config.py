"""Configuration management for Legal Case Researcher."""
import os
import yaml
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class LLMConfig:
    model: str = "gemma4:latest"
    temperature: float = 0.3
    max_tokens: int = 4096
    ollama_host: str = "http://localhost:11434"

@dataclass
class AppConfig:
    name: str = "Legal Case Researcher"
    version: str = "1.0.0"
    llm: LLMConfig = field(default_factory=LLMConfig)
    log_level: str = "INFO"

def load_config(config_path: Optional[str] = None) -> AppConfig:
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    config = AppConfig()
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f) or {}
        if 'llm' in data:
            config.llm = LLMConfig(**data['llm'])
        if 'app' in data:
            config.name = data['app'].get('name', config.name)
            config.version = data['app'].get('version', config.version)
        config.log_level = data.get('logging', {}).get('level', config.log_level)
    config.llm.ollama_host = os.environ.get('OLLAMA_HOST', config.llm.ollama_host)
    config.llm.model = os.environ.get('OLLAMA_MODEL', config.llm.model)
    return config
