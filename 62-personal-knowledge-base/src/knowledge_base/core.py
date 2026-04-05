#!/usr/bin/env python3
"""Personal Knowledge Base - Core functions for note storage and semantic search."""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import json
import re
import logging
from datetime import datetime
from collections import Counter

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')


def load_config() -> dict:
    """Load configuration from config.yaml, falling back to sensible defaults."""
    defaults = {
        "app": {"name": "Personal Knowledge Base", "version": "1.0.0", "log_level": "INFO", "data_dir": "./data"},
        "knowledge_base": {"max_notes": 10000, "default_tags": [], "search_limit": 20,
                           "backup_enabled": True, "backup_interval_hours": 24},
        "templates": {},
        "llm": {"model": "llama3", "temperature": 0.3, "system_prompt": "You are a knowledge base search assistant."},
    }
    resolved = os.path.normpath(os.path.abspath(CONFIG_PATH))
    if os.path.exists(resolved):
        try:
            with open(resolved, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
            for section, values in defaults.items():
                if section not in data:
                    data[section] = values
                elif isinstance(values, dict):
                    for k, v in values.items():
                        data[section].setdefault(k, v)
            logger.debug("Loaded config from %s", resolved)
            return data
        except Exception as exc:
            logger.warning("Failed to load config: %s – using defaults", exc)
    return defaults


config = load_config()
logging.basicConfig(
    level=getattr(logging, config["app"].get("log_level", "INFO"), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

# Resolve data directory and KB file
_data_dir = os.path.normpath(os.path.join(
    os.path.dirname(__file__), '..', '..', config["app"]["data_dir"]
))
os.makedirs(_data_dir, exist_ok=True)
KB_FILE = os.path.join(_data_dir, "knowledge_base.json")

# ---------------------------------------------------------------------------
# Core CRUD
# ---------------------------------------------------------------------------


def load_kb() -> dict:
    """Load the knowledge base from JSON file."""
    if os.path.exists(KB_FILE):
        try:
            with open(KB_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as exc:
            logger.error("Failed to load KB: %s", exc)
            return {"notes": [], "metadata": {"created": datetime.now().isoformat()}}
    return {"notes": [], "metadata": {"created": datetime.now().isoformat()}}


def save_kb(kb: dict) -> None:
    """Save the knowledge base to JSON file."""
    kb["metadata"]["updated"] = datetime.now().isoformat()
    with open(KB_FILE, 'w', encoding='utf-8') as f:
        json.dump(kb, f, indent=2)
    logger.debug("KB saved with %d notes", len(kb["notes"]))


def add_note(title: str, content: str, tags: list[str] | None = None) -> dict:
    """Add a note to the knowledge base."""
    kb = load_kb()
    max_notes = config["knowledge_base"]["max_notes"]
    if len(kb["notes"]) >= max_notes:
        raise ValueError(f"Knowledge base limit reached ({max_notes} notes)")

    note_id = max((n["id"] for n in kb["notes"]), default=0) + 1
    note = {
        "id": note_id,
        "title": title,
        "content": content,
        "tags": tags or [],
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
    }
    kb["notes"].append(note)
    save_kb(kb)
    logger.info("Added note #%d: %s", note_id, title)
    return note


def delete_note(note_id: int) -> bool:
    """Delete a note by ID. Returns True if deleted, False if not found."""
    kb = load_kb()
    original_len = len(kb["notes"])
    kb["notes"] = [n for n in kb["notes"] if n["id"] != note_id]
    if len(kb["notes"]) == original_len:
        return False
    save_kb(kb)
    logger.info("Deleted note #%d", note_id)
    return True


def get_note(note_id: int) -> dict | None:
    """Return a single note by ID or None."""
    kb = load_kb()
    for n in kb["notes"]:
        if n["id"] == note_id:
            return n
    return None


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------


def display_notes(notes: list[dict]) -> None:
    """Display notes in a formatted Rich table."""
    from rich.console import Console
    from rich.table import Table

    console = Console()
    table = Table(title="📚 Knowledge Base", show_lines=True)
    table.add_column("ID", style="cyan", width=5)
    table.add_column("Title", style="white", min_width=20)
    table.add_column("Tags", style="green", min_width=15)
    table.add_column("Created", style="yellow", min_width=12)
    table.add_column("Preview", style="dim", max_width=40)

    for note in notes:
        created = note.get("created", "N/A")[:10]
        content = note.get("content", "")
        preview = (content[:40] + "...") if len(content) > 40 else content
        table.add_row(
            str(note["id"]),
            note["title"],
            ", ".join(note.get("tags", [])),
            created,
            preview,
        )
    console.print(table)


# ---------------------------------------------------------------------------
# AI-powered search & summarisation
# ---------------------------------------------------------------------------


def search_notes(query: str) -> str:
    """Search notes semantically using AI."""
    kb = load_kb()
    if not kb["notes"]:
        return "No notes in knowledge base. Add some with the 'add' command."

    notes_text = "\n\n".join(
        f"Note #{n['id']}: {n['title']}\nTags: {', '.join(n.get('tags', []))}\nContent: {n['content']}"
        for n in kb["notes"]
    )

    prompt = (
        f'Search the following knowledge base for information related to: "{query}"\n\n'
        f"Knowledge Base:\n{notes_text}\n\n"
        "Please:\n"
        "1. Identify the most relevant notes\n"
        "2. Summarize the relevant information\n"
        "3. Show connections between related notes\n"
        "4. Suggest related topics to explore\n\n"
        "Format your response in markdown."
    )
    return generate(
        prompt=prompt,
        system_prompt=config["llm"]["system_prompt"],
        temperature=config["llm"]["temperature"],
    )


def summarize_kb() -> str:
    """Generate a summary of the entire knowledge base."""
    kb = load_kb()
    if not kb["notes"]:
        return "Knowledge base is empty."

    notes_text = "\n\n".join(
        f"- {n['title']}: {n['content'][:200]}" for n in kb["notes"]
    )

    prompt = (
        f"Summarize this knowledge base:\n\n{notes_text}\n\n"
        "Provide:\n"
        "1. **Overview**: Main topics covered\n"
        "2. **Key Insights**: Most important information\n"
        "3. **Knowledge Gaps**: Areas that could use more notes\n"
        "4. **Connections**: How different notes relate to each other"
    )
    return generate(
        prompt=prompt,
        system_prompt="You are a knowledge organization expert.",
        temperature=0.5,
    )


# ---------------------------------------------------------------------------
# Tag system
# ---------------------------------------------------------------------------


def get_all_tags(kb: dict | None = None) -> dict[str, int]:
    """Return a mapping of tag → count across all notes."""
    if kb is None:
        kb = load_kb()
    counter: Counter = Counter()
    for note in kb["notes"]:
        for tag in note.get("tags", []):
            counter[tag] += 1
    return dict(counter.most_common())


def tag_cloud() -> list[tuple[str, int]]:
    """Return a sorted list of (tag, count) tuples for tag-cloud display."""
    return sorted(get_all_tags().items(), key=lambda x: (-x[1], x[0]))


def get_notes_by_tag(tag: str) -> list[dict]:
    """Return all notes that have a given tag."""
    kb = load_kb()
    return [n for n in kb["notes"] if tag in n.get("tags", [])]


# ---------------------------------------------------------------------------
# Backlinks
# ---------------------------------------------------------------------------


def find_backlinks(note_id: int) -> list[dict]:
    """Find notes whose content references the given note (by title mention)."""
    kb = load_kb()
    target = get_note(note_id)
    if target is None:
        return []

    title_lower = target["title"].lower()
    backlinks = []
    for note in kb["notes"]:
        if note["id"] == note_id:
            continue
        if title_lower in note.get("content", "").lower() or title_lower in note.get("title", "").lower():
            backlinks.append(note)
    return backlinks


def find_all_backlinks() -> dict[int, list[int]]:
    """Return a mapping of note_id → [ids of notes that reference it]."""
    kb = load_kb()
    result: dict[int, list[int]] = {}
    for target in kb["notes"]:
        title_lower = target["title"].lower()
        refs = []
        for note in kb["notes"]:
            if note["id"] == target["id"]:
                continue
            if title_lower in note.get("content", "").lower():
                refs.append(note["id"])
        if refs:
            result[target["id"]] = refs
    return result


# ---------------------------------------------------------------------------
# Full-text search (no LLM)
# ---------------------------------------------------------------------------


def search_fulltext(query: str, case_sensitive: bool = False) -> list[dict]:
    """Simple keyword search across titles, content, and tags."""
    kb = load_kb()
    q = query if case_sensitive else query.lower()
    results = []
    for note in kb["notes"]:
        haystack = (
            f"{note['title']} {note['content']} {' '.join(note.get('tags', []))}"
        )
        if not case_sensitive:
            haystack = haystack.lower()
        if q in haystack:
            results.append(note)
    limit = config["knowledge_base"]["search_limit"]
    return results[:limit]


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

DEFAULT_TEMPLATES: dict[str, dict[str, str]] = {
    "meeting_notes": {
        "title": "Meeting Notes - {date}",
        "content": "## Attendees\n\n## Agenda\n\n## Discussion\n\n## Action Items\n",
    },
    "book_review": {
        "title": "Book Review - {title}",
        "content": "## Summary\n\n## Key Takeaways\n\n## Rating\n\n## Recommendations\n",
    },
    "project_plan": {
        "title": "Project Plan - {name}",
        "content": "## Objectives\n\n## Timeline\n\n## Resources\n\n## Risks\n",
    },
}


def get_templates() -> dict[str, dict[str, str]]:
    """Return available note templates (config overrides + defaults)."""
    templates = dict(DEFAULT_TEMPLATES)
    cfg_templates = config.get("templates", {})
    if cfg_templates:
        templates.update(cfg_templates)
    return templates


def get_template(name: str) -> dict[str, str] | None:
    """Get a single template by name."""
    return get_templates().get(name)


def apply_template(name: str, **kwargs: str) -> dict[str, str] | None:
    """Apply a template, substituting placeholders with provided kwargs.

    Returns a dict with ``title`` and ``content`` keys, or None if not found.
    """
    tpl = get_template(name)
    if tpl is None:
        return None
    title = tpl["title"]
    content = tpl["content"]
    for key, value in kwargs.items():
        title = title.replace(f"{{{key}}}", value)
        content = content.replace(f"{{{key}}}", value)
    return {"title": title, "content": content}


# ---------------------------------------------------------------------------
# Export / Import (Markdown)
# ---------------------------------------------------------------------------


def export_notes(filepath: str | None = None) -> str:
    """Export all notes to a Markdown file. Returns the filepath used."""
    kb = load_kb()
    if filepath is None:
        filepath = os.path.join(_data_dir, "knowledge_base_export.md")

    lines: list[str] = ["# Knowledge Base Export\n"]
    lines.append(f"_Exported on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n")

    for note in kb["notes"]:
        lines.append(f"## [{note['id']}] {note['title']}\n")
        lines.append(f"**Tags:** {', '.join(note.get('tags', [])) or 'none'}\n")
        lines.append(f"**Created:** {note.get('created', 'N/A')}\n\n")
        lines.append(f"{note['content']}\n\n")
        lines.append("---\n\n")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    logger.info("Exported %d notes to %s", len(kb["notes"]), filepath)
    return filepath


def import_notes(filepath: str) -> int:
    """Import notes from a Markdown file exported by export_notes.

    Returns the number of notes imported.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Import file not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(
        r"## \[(\d+)\] (.+?)\n"
        r"\*\*Tags:\*\* (.+?)\n"
        r"\*\*Created:\*\* (.+?)\n\n"
        r"(.*?)\n\n---",
        re.DOTALL,
    )

    count = 0
    for match in pattern.finditer(content):
        title = match.group(2).strip()
        tags_str = match.group(3).strip()
        tags = [t.strip() for t in tags_str.split(',') if t.strip() and t.strip() != 'none']
        body = match.group(5).strip()
        add_note(title, body, tags)
        count += 1

    logger.info("Imported %d notes from %s", count, filepath)
    return count
