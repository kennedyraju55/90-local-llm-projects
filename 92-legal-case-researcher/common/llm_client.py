"""
Common Ollama/Gemma 4 Client Utility
Shared across all 90 projects for consistent LLM interaction.
"""

import requests
import json
import sys
from typing import Optional, Generator


OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "gemma4"


def check_ollama_running() -> bool:
    try:
        resp = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        return resp.status_code == 200
    except requests.ConnectionError:
        return False


def list_models() -> list:
    try:
        resp = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        data = resp.json()
        return [m["name"] for m in data.get("models", [])]
    except Exception:
        return []


def chat(messages, model=DEFAULT_MODEL, system_prompt=None, temperature=0.7, max_tokens=2048):
    if system_prompt:
        messages = [{"role": "system", "content": system_prompt}] + messages
    payload = {"model": model, "messages": messages, "stream": False, "options": {"temperature": temperature, "num_predict": max_tokens}}
    try:
        resp = requests.post(f"{OLLAMA_BASE_URL}/api/chat", json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["message"]["content"]
    except requests.exceptions.ConnectionError:
        print("Error: Ollama is not running. Start it with: ollama serve")
        sys.exit(1)
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        sys.exit(1)


def generate(prompt, model=DEFAULT_MODEL, system_prompt=None, temperature=0.7, max_tokens=2048):
    payload = {"model": model, "prompt": prompt, "stream": False, "options": {"temperature": temperature, "num_predict": max_tokens}}
    if system_prompt:
        payload["system"] = system_prompt
    try:
        resp = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["response"]
    except requests.exceptions.ConnectionError:
        print("Error: Ollama is not running. Start it with: ollama serve")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
