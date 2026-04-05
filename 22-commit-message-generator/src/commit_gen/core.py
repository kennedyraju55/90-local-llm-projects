"""Core business logic for Commit Gen."""

import os
import sys
import logging
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import CommitConfig, load_config, COMMIT_EMOJIS
from .utils import truncate_diff, add_emoji_to_message

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an expert at writing git commit messages following the Conventional Commits specification.

Given a git diff, generate a clear, concise commit message with:
1. Type: feat, fix, docs, style, refactor, perf, test, build, ci, chore
2. Optional scope in parentheses
3. Short description (50 chars max for subject line)
4. Optional body with more detail
5. Optional footer for breaking changes

Format:
```
type(scope): short description

Longer description if needed, explaining what and why.

BREAKING CHANGE: description (if applicable)
```

Provide exactly {num} commit message options ranked by quality."""


def generate_commit_messages(
    diff: str,
    msg_type: str = "",
    config: Optional[CommitConfig] = None,
) -> str:
    """Generate conventional commit messages from a diff."""
    config = config or load_config()
    truncated = truncate_diff(diff, config.max_diff_chars)

    type_hint = ""
    if msg_type:
        type_hint = f"\nThe commit type should be: {msg_type}"

    system = SYSTEM_PROMPT.replace("{num}", str(config.num_suggestions))

    prompt = f"""Generate conventional commit messages for the following git diff:{type_hint}

```diff
{truncated}
```

Provide {config.num_suggestions} options, each clearly numbered."""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating commit messages (type=%s)", msg_type or "auto")

    response = chat(
        messages,
        system_prompt=system,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    if config.use_emoji:
        lines = response.splitlines()
        result_lines = []
        for line in lines:
            stripped = line.strip()
            modified = add_emoji_to_message(stripped, COMMIT_EMOJIS)
            result_lines.append(modified if modified != stripped else line)
        response = "\n".join(result_lines)

    return response


def generate_batch_messages(
    diffs: list[dict],
    config: Optional[CommitConfig] = None,
) -> list[dict]:
    """Generate commit messages for multiple diffs (batch mode)."""
    config = config or load_config()
    results = []
    for item in diffs:
        diff = item.get("diff", "")
        name = item.get("name", "unknown")
        if diff.strip():
            msg = generate_commit_messages(diff, config=config)
            results.append({"name": name, "messages": msg})
            logger.info("Generated messages for: %s", name)
        else:
            results.append({"name": name, "messages": "No changes found."})
    return results
