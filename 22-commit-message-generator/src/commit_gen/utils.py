"""Utility helpers for Commit Gen."""

import subprocess
import sys
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def get_git_diff(staged_only: bool = True) -> str:
    """Get the current git diff."""
    try:
        cmd = ["git", "diff"]
        if staged_only:
            cmd.append("--staged")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except FileNotFoundError:
        logger.error("git is not installed or not in PATH")
        return ""
    except subprocess.TimeoutExpired:
        logger.error("git diff timed out")
        return ""


def get_git_stat(staged_only: bool = True) -> str:
    """Get git diff --stat for a summary."""
    try:
        cmd = ["git", "diff", "--stat"]
        if staged_only:
            cmd.append("--staged")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except Exception:
        return ""


def get_git_staged_files() -> list[str]:
    """Get list of staged file names."""
    try:
        result = subprocess.run(
            ["git", "diff", "--staged", "--name-only"],
            capture_output=True, text=True, timeout=30,
        )
        return [f for f in result.stdout.strip().splitlines() if f]
    except Exception:
        return []


def get_git_branch() -> str:
    """Get the current git branch name."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def read_diff_from_stdin() -> str:
    """Read diff from stdin if available."""
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def truncate_diff(diff: str, max_chars: int = 4000) -> str:
    """Truncate diff to max_chars, preserving structure."""
    if len(diff) <= max_chars:
        return diff
    return diff[:max_chars] + "\n... (diff truncated)"


def add_emoji_to_message(message: str, emojis: dict) -> str:
    """Add emoji prefix to conventional commit message."""
    for commit_type, emoji in emojis.items():
        if message.startswith(f"{commit_type}(") or message.startswith(f"{commit_type}:"):
            return f"{emoji} {message}"
    return message
