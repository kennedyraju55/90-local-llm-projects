"""Core business logic for IT Helpdesk Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
from common.llm_client import chat, check_ollama_running  # noqa: E402

SYSTEM_PROMPT = """You are an expert IT Helpdesk Support Agent. Your role is to:
1. Diagnose technical issues based on user descriptions
2. Provide step-by-step troubleshooting instructions
3. Suggest solutions for hardware, software, network, and security problems
4. Escalate complex issues by recommending the user contact senior support
5. Always be patient, clear, and professional

Guidelines:
- Ask clarifying questions when the issue is unclear
- Provide numbered steps for solutions
- Mention the operating system or platform when relevant
- Warn users before suggesting actions that could cause data loss
- If you're unsure, say so and recommend professional help"""

CATEGORIES = {
    "1": ("🖥️ Hardware Issues", "computer hardware, peripherals, monitors, keyboards"),
    "2": ("💾 Software Issues", "application errors, installations, updates, crashes"),
    "3": ("🌐 Network Issues", "WiFi, ethernet, VPN, internet connectivity"),
    "4": ("🔒 Security Issues", "passwords, malware, phishing, account access"),
    "5": ("📧 Email Issues", "email setup, sending/receiving problems, spam"),
    "6": ("🖨️ Printer Issues", "printer setup, print jobs, drivers"),
    "7": ("💬 General Question", "any other IT-related question"),
}


def get_response(
    user_message: str,
    history: list[dict],
    model: str = "gemma4",
    temperature: float = 0.7,
) -> str:
    """Get a response from the IT helpdesk bot."""
    messages = history + [{"role": "user", "content": user_message}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature)
