"""Configuration management for Differential Diagnosis Assistant."""
import os
import yaml
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "model": "gemma4",
    "temperature": 0.3,
    "max_tokens": 2048,
    "log_level": "INFO",
    "ollama_url": os.getenv("OLLAMA_HOST", "http://localhost:11434"),
}

def load_config(config_path: str = None) -> Dict[str, Any]:
    """Load configuration from YAML file with defaults."""
    config = DEFAULT_CONFIG.copy()
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    try:
        with open(config_path, 'r') as f:
            user_config = yaml.safe_load(f) or {}
        config.update(user_config)
    except (FileNotFoundError, yaml.YAMLError):
        pass
    return config
