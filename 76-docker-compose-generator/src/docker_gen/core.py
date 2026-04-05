"""Core business logic for Docker Compose generation."""

import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


def load_config() -> dict:
    """Load application configuration from config.yaml."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning("config.yaml not found, using defaults")
        return {}


CONFIG = load_config()

SYSTEM_PROMPT = """You are a DevOps engineer expert in Docker and containerization.
Generate production-ready docker-compose.yml files based on user requirements.

Follow these best practices:
1. Use specific image versions, not 'latest'
2. Add health checks where appropriate
3. Set resource limits for production environments
4. Use named volumes for data persistence
5. Configure proper networking between services
6. Add restart policies
7. Use environment variables for configuration
8. Add proper labels and comments
9. Follow the principle of least privilege

Output ONLY valid YAML for docker-compose files unless asked for explanation."""

# ---------------------------------------------------------------------------
# Service Catalog
# ---------------------------------------------------------------------------

SERVICE_CATALOG = {
    "databases": {
        "postgres": {"image": "postgres:16-alpine", "port": 5432, "category": "database"},
        "mysql": {"image": "mysql:8.0", "port": 3306, "category": "database"},
        "mongodb": {"image": "mongo:7", "port": 27017, "category": "database"},
        "redis": {"image": "redis:7-alpine", "port": 6379, "category": "cache"},
        "mariadb": {"image": "mariadb:11", "port": 3306, "category": "database"},
    },
    "web_servers": {
        "nginx": {"image": "nginx:1.25-alpine", "port": 80, "category": "proxy"},
        "traefik": {"image": "traefik:v3.0", "port": 80, "category": "proxy"},
        "caddy": {"image": "caddy:2-alpine", "port": 80, "category": "proxy"},
        "apache": {"image": "httpd:2.4-alpine", "port": 80, "category": "proxy"},
    },
    "messaging": {
        "rabbitmq": {"image": "rabbitmq:3-management-alpine", "port": 5672, "category": "messaging"},
        "kafka": {"image": "confluentinc/cp-kafka:7.5.0", "port": 9092, "category": "messaging"},
        "nats": {"image": "nats:2-alpine", "port": 4222, "category": "messaging"},
    },
    "monitoring": {
        "prometheus": {"image": "prom/prometheus:v2.48.0", "port": 9090, "category": "monitoring"},
        "grafana": {"image": "grafana/grafana:10.2.0", "port": 3000, "category": "monitoring"},
        "elasticsearch": {"image": "elasticsearch:8.11.0", "port": 9200, "category": "search"},
        "kibana": {"image": "kibana:8.11.0", "port": 5601, "category": "monitoring"},
    },
    "runtimes": {
        "python": {"image": "python:3.12-slim", "port": 8000, "category": "runtime"},
        "node": {"image": "node:20-alpine", "port": 3000, "category": "runtime"},
        "golang": {"image": "golang:1.21-alpine", "port": 8080, "category": "runtime"},
        "java": {"image": "eclipse-temurin:21-jre-alpine", "port": 8080, "category": "runtime"},
    },
}

COMMON_STACKS = {
    "mean": "MongoDB, Express.js, Angular, Node.js",
    "mern": "MongoDB, Express.js, React, Node.js",
    "lamp": "Linux, Apache, MySQL, PHP",
    "lemp": "Linux, Nginx, MySQL, PHP",
    "django": "Python Django with PostgreSQL and Nginx",
    "flask": "Python Flask with PostgreSQL and Redis",
    "rails": "Ruby on Rails with PostgreSQL and Redis",
    "spring": "Java Spring Boot with MySQL",
    "wordpress": "WordPress with MySQL and Nginx",
    "elk": "Elasticsearch, Logstash, Kibana",
}

NETWORK_TEMPLATES = {
    "simple": {"driver": "bridge"},
    "isolated": {"driver": "bridge", "internal": True},
    "overlay": {"driver": "overlay", "attachable": True},
}

ENV_PROFILES = {
    "development": {
        "restart": "unless-stopped",
        "logging": False,
        "resource_limits": False,
        "health_checks": False,
        "debug_ports": True,
        "hot_reload": True,
    },
    "staging": {
        "restart": "on-failure",
        "logging": True,
        "resource_limits": True,
        "health_checks": True,
        "debug_ports": False,
        "hot_reload": False,
    },
    "production": {
        "restart": "always",
        "logging": True,
        "resource_limits": True,
        "health_checks": True,
        "debug_ports": False,
        "hot_reload": False,
    },
}


def get_service_catalog() -> dict:
    """Return the full service catalog organized by category."""
    return SERVICE_CATALOG


def get_flat_catalog() -> dict:
    """Return a flat dictionary of all services."""
    flat = {}
    for category, services in SERVICE_CATALOG.items():
        for name, info in services.items():
            flat[name] = {**info, "group": category}
    return flat


def get_env_profile(env: str) -> dict:
    """Return configuration profile for an environment."""
    return ENV_PROFILES.get(env, ENV_PROFILES["development"])


def generate_compose(
    stack_description: str,
    env: str = "development",
    services: Optional[list] = None,
    network_mode: str = "simple",
) -> str:
    """Generate a Docker Compose file from a stack description.

    Args:
        stack_description: Natural language description of the desired stack.
        env: Target environment (development/staging/production).
        services: Optional list of specific services from catalog.
        network_mode: Network configuration template.

    Returns:
        Generated docker-compose.yml content.
    """
    logger.info("Generating compose for stack=%s env=%s", stack_description, env)

    stack_lower = stack_description.lower()
    for key, desc in COMMON_STACKS.items():
        if key in stack_lower:
            stack_description = f"{stack_description} ({desc})"
            break

    profile = get_env_profile(env)
    service_hint = ""
    if services:
        catalog = get_flat_catalog()
        selected = {s: catalog[s] for s in services if s in catalog}
        service_hint = f"\nInclude these catalog services: {selected}"

    network_hint = f"\nNetwork mode: {NETWORK_TEMPLATES.get(network_mode, NETWORK_TEMPLATES['simple'])}"

    env_requirements = []
    if profile["resource_limits"]:
        env_requirements.append("- Add resource limits (CPU/memory)")
    if profile["health_checks"]:
        env_requirements.append("- Add health checks for every service")
    if profile["logging"]:
        env_requirements.append("- Add logging configuration (json-file driver, max-size)")
    if profile["hot_reload"]:
        env_requirements.append("- Add hot reload volumes for development")
    if profile["debug_ports"]:
        env_requirements.append("- Expose debug ports")
    env_requirements.append(f"- Set restart policy: {profile['restart']}")

    env_reqs_str = "\n".join(env_requirements)

    prompt = f"""Generate a complete docker-compose.yml for the following stack:
Stack: {stack_description}
Environment: {env}
{service_hint}{network_hint}

Requirements for {env} environment:
{env_reqs_str}

Output only the YAML content, no explanation."""

    result = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=3000,
    )
    logger.info("Compose generation complete")
    return result


def explain_compose(compose_content: str) -> str:
    """Explain an existing Docker Compose file.

    Args:
        compose_content: Content of a docker-compose.yml file.

    Returns:
        Human-readable explanation.
    """
    logger.info("Explaining compose file (%d chars)", len(compose_content))
    prompt = f"""Explain this docker-compose.yml file in plain English.
Describe each service, its purpose, configuration, and how services interact.

{compose_content}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.4,
        max_tokens=2048,
    )


def extract_yaml(text: str) -> str:
    """Extract YAML content from LLM response.

    Args:
        text: Raw LLM response that may contain markdown fences.

    Returns:
        Clean YAML content.
    """
    for fence in ["```yaml", "```yml", "```"]:
        if fence in text:
            start = text.index(fence) + len(fence)
            remaining = text[start:]
            end = remaining.index("```") if "```" in remaining else len(remaining)
            return remaining[:end].strip()
    return text.strip()


def validate_compose(yaml_content: str) -> dict:
    """Validate generated Docker Compose YAML.

    Args:
        yaml_content: YAML string to validate.

    Returns:
        Dict with 'valid' bool and 'errors' list.
    """
    errors = []
    try:
        data = yaml.safe_load(yaml_content)
        if not isinstance(data, dict):
            errors.append("Root element is not a mapping")
        elif "services" not in data:
            errors.append("Missing 'services' key")
    except yaml.YAMLError as exc:
        errors.append(f"YAML parse error: {exc}")

    return {"valid": len(errors) == 0, "errors": errors}
