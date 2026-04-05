#!/usr/bin/env python3
"""Family Story Creator - Core business logic for creating personalized family stories."""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import json
import logging
import uuid
from datetime import datetime

import yaml

# LLM client import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants & Templates
# ---------------------------------------------------------------------------

STORY_STYLES = {
    "heartwarming": "Write in a warm, emotional, feel-good style that celebrates family bonds.",
    "humorous": "Write with humor, funny anecdotes, and light-hearted observations.",
    "adventurous": "Write as an exciting adventure story with dramatic moments.",
    "nostalgic": "Write with a nostalgic, reflective tone that cherishes memories.",
    "fairy-tale": "Write in a fairy-tale style with magical elements woven into real events.",
    "poetic": "Write with poetic language, rich imagery, and lyrical prose.",
}

CHARACTER_PROFILES = {
    "fields": ["name", "age", "personality", "relationship", "appearance"],
    "personality_traits": [
        "cheerful", "wise", "adventurous", "gentle", "funny",
        "caring", "brave", "creative", "patient", "energetic",
    ],
    "relationships": [
        "mother", "father", "grandmother", "grandfather",
        "son", "daughter", "sister", "brother",
        "aunt", "uncle", "cousin", "friend",
    ],
}

CHAPTER_TEMPLATES = {
    "introduction": "Set the scene and introduce the family members. Establish the setting and tone.",
    "rising_action": "Build excitement and develop the story with key events and interactions.",
    "climax": "Bring the story to its most exciting or emotional peak moment.",
    "resolution": "Wrap up the story with a satisfying and meaningful conclusion.",
    "epilogue": "Reflect on the events and hint at what the future holds for the family.",
}

DEFAULT_CONFIG = {
    "llm": {
        "model": "llama3.2",
        "temperature": 0.8,
        "max_tokens": 3000,
    },
    "stories_file": "family_stories.json",
    "default_style": "heartwarming",
    "default_length": "medium",
    "export": {
        "formats": ["markdown", "html"],
        "output_dir": "exports",
    },
    "logging": {
        "level": "INFO",
        "file": "family_story.log",
    },
}

LENGTH_GUIDE = {
    "short": "Write a short story of about 300-500 words.",
    "medium": "Write a medium-length story of about 500-800 words.",
    "long": "Write a detailed story of about 800-1200 words.",
}


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def load_config(config_path: str = None) -> dict:
    """Load configuration from a YAML file, falling back to defaults."""
    config = dict(DEFAULT_CONFIG)
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = yaml.safe_load(f) or {}
            # Merge top-level and nested keys
            for key, value in user_config.items():
                if isinstance(value, dict) and isinstance(config.get(key), dict):
                    config[key] = {**config[key], **value}
                else:
                    config[key] = value
            logger.info("Loaded config from %s", config_path)
        except Exception as exc:
            logger.warning("Failed to load config from %s: %s", config_path, exc)
    return config


def _setup_logging(config: dict) -> None:
    """Configure logging based on config."""
    log_cfg = config.get("logging", {})
    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO")),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            *(
                [logging.FileHandler(log_cfg["file"])]
                if log_cfg.get("file")
                else []
            ),
        ],
    )


# ---------------------------------------------------------------------------
# Story Persistence
# ---------------------------------------------------------------------------

def load_stories(stories_file: str = None) -> list[dict]:
    """Load saved stories from JSON file."""
    path = stories_file or DEFAULT_CONFIG["stories_file"]
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                stories = json.load(f)
            logger.debug("Loaded %d stories from %s", len(stories), path)
            return stories
        except (json.JSONDecodeError, IOError) as exc:
            logger.error("Error loading stories: %s", exc)
            return []
    return []


def save_story(story: dict, stories_file: str = None) -> dict:
    """Save a new story and return it with generated id and timestamp."""
    path = stories_file or DEFAULT_CONFIG["stories_file"]
    stories = load_stories(path)
    story["id"] = str(uuid.uuid4())[:8]
    story["created"] = datetime.now().isoformat()
    stories.append(story)
    with open(path, "w") as f:
        json.dump(stories, f, indent=2)
    logger.info("Saved story %s to %s", story["id"], path)
    return story


def delete_story(story_id: str, stories_file: str = None) -> bool:
    """Delete a story by its id. Returns True if found and deleted."""
    path = stories_file or DEFAULT_CONFIG["stories_file"]
    stories = load_stories(path)
    original_len = len(stories)
    stories = [s for s in stories if str(s.get("id")) != str(story_id)]
    if len(stories) == original_len:
        logger.warning("Story %s not found", story_id)
        return False
    with open(path, "w") as f:
        json.dump(stories, f, indent=2)
    logger.info("Deleted story %s", story_id)
    return True


# ---------------------------------------------------------------------------
# Character Builder
# ---------------------------------------------------------------------------

def create_character(
    name: str,
    age: int = None,
    personality: str = "",
    relationship: str = "",
    appearance: str = "",
) -> dict:
    """Build a structured character profile for a family member."""
    character = {
        "name": name,
        "age": age,
        "personality": personality,
        "relationship": relationship,
        "appearance": appearance,
    }
    logger.debug("Created character profile for %s", name)
    return character


def _format_characters(members: str | list) -> str:
    """Format member info into a prompt-friendly string."""
    if isinstance(members, list):
        parts = []
        for m in members:
            if isinstance(m, dict):
                desc = m.get("name", "Unknown")
                extras = []
                if m.get("age"):
                    extras.append(f"age {m['age']}")
                if m.get("relationship"):
                    extras.append(m["relationship"])
                if m.get("personality"):
                    extras.append(m["personality"])
                if m.get("appearance"):
                    extras.append(m["appearance"])
                if extras:
                    desc += f" ({', '.join(extras)})"
                parts.append(desc)
            else:
                parts.append(str(m))
        return ", ".join(parts)
    return str(members)


# ---------------------------------------------------------------------------
# Story Creation
# ---------------------------------------------------------------------------

def create_story(
    members: str | list,
    event: str,
    style: str = "heartwarming",
    details: str = "",
    photos: str = "",
    length: str = "medium",
    config: dict = None,
) -> str:
    """Create a personalized family story using AI."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", {})
    style_instruction = STORY_STYLES.get(style, STORY_STYLES["heartwarming"])
    members_text = _format_characters(members)

    prompt = f"""Create a personalized family story with these details:

**Family Members**: {members_text}
**Event/Occasion**: {event}
{f'**Additional Details**: {details}' if details else ''}
{f'**Photo Descriptions**: {photos}' if photos else ''}

Style: {style_instruction}
{LENGTH_GUIDE.get(length, LENGTH_GUIDE['medium'])}

Requirements:
1. Use the actual family member names naturally in the story
2. Make the event the central focus of the narrative
3. Include realistic dialogue between family members
4. Add sensory details (sights, sounds, smells) to bring scenes alive
5. End with a meaningful reflection or heartwarming moment
6. Make it feel personal and authentic

Write the story in markdown format with a creative title."""

    logger.info("Creating %s %s story about '%s'", length, style, event)
    return generate(
        prompt=prompt,
        system_prompt=(
            "You are a gifted family storyteller who creates beautiful, "
            "personalized narratives from real family memories and events. "
            "Your stories are touching, authentic, and treasured keepsakes."
        ),
        temperature=llm.get("temperature", 0.8),
        max_tokens=llm.get("max_tokens", 3000),
    )


# ---------------------------------------------------------------------------
# Chapter & Book
# ---------------------------------------------------------------------------

def create_chapter(
    chapter_num: int,
    title: str,
    members: str | list,
    events: str,
    style: str = "heartwarming",
    config: dict = None,
) -> str:
    """Create a single chapter of a multi-chapter story."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", {})
    style_instruction = STORY_STYLES.get(style, STORY_STYLES["heartwarming"])
    members_text = _format_characters(members)

    prompt = f"""Write Chapter {chapter_num}: "{title}" of a family story book.

**Family Members**: {members_text}
**Chapter Events**: {events}

Style: {style_instruction}

Requirements:
1. Start with "## Chapter {chapter_num}: {title}"
2. Write 400-600 words for this chapter
3. Use the family member names naturally
4. End the chapter with a hook or transition to the next
5. Make it vivid with dialogue and sensory details"""

    logger.info("Creating chapter %d: %s", chapter_num, title)
    return generate(
        prompt=prompt,
        system_prompt=(
            "You are a gifted family storyteller writing a chapter of a "
            "family story book. Each chapter should flow naturally and "
            "contribute to the overall narrative."
        ),
        temperature=llm.get("temperature", 0.8),
        max_tokens=llm.get("max_tokens", 3000),
    )


def create_book(
    title: str,
    chapters: list[dict],
    members: str | list,
    config: dict = None,
) -> dict:
    """Create a full multi-chapter story book.

    Args:
        title: Book title.
        chapters: List of dicts with 'title' and 'events' keys.
        members: Family members (string or list of character dicts).
        config: Optional configuration dict.

    Returns:
        dict with keys: title, toc (list of chapter titles), chapters (list of chapter texts).
    """
    cfg = config or DEFAULT_CONFIG
    style = cfg.get("default_style", "heartwarming")
    toc = [ch["title"] for ch in chapters]
    chapter_texts = []

    for idx, ch in enumerate(chapters, 1):
        text = create_chapter(
            chapter_num=idx,
            title=ch["title"],
            members=members,
            events=ch["events"],
            style=style,
            config=cfg,
        )
        chapter_texts.append(text)

    logger.info("Created book '%s' with %d chapters", title, len(chapters))
    return {"title": title, "toc": toc, "chapters": chapter_texts}


# ---------------------------------------------------------------------------
# Continuation & Poem
# ---------------------------------------------------------------------------

def continue_story(existing_story: str, prompt: str, config: dict = None) -> str:
    """Continue or expand an existing story."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", {})

    full_prompt = f"""Here is an existing family story:

{existing_story}

Please continue the story with this direction: {prompt}

Maintain the same style, characters, and tone. Add 300-500 more words."""

    logger.info("Continuing story with prompt: %s", prompt[:50])
    return generate(
        prompt=full_prompt,
        system_prompt="You are a gifted family storyteller continuing a narrative.",
        temperature=llm.get("temperature", 0.8),
        max_tokens=llm.get("max_tokens", 3000),
    )


def create_poem(
    members: str,
    event: str,
    style: str = "rhyming",
    config: dict = None,
) -> str:
    """Create a family poem about an event."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", {})

    prompt = f"""Create a beautiful {style} poem about this family event:

Family Members: {members}
Event: {event}

Write a poem of 4-6 stanzas that:
1. Mentions each family member by name
2. Captures the spirit of the event
3. Is emotionally moving and personal
4. Has a memorable final stanza"""

    logger.info("Creating %s poem about '%s'", style, event)
    return generate(
        prompt=prompt,
        system_prompt="You are a poet who creates personalized family poems.",
        temperature=llm.get("temperature", 0.8),
        max_tokens=llm.get("max_tokens", 3000),
    )


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------

def export_story(story: dict, format: str = "markdown") -> str:
    """Export a story to the specified format.

    Args:
        story: dict with at least 'story' key; optionally 'members', 'event', 'style', 'created'.
        format: 'markdown' or 'html'.

    Returns:
        Formatted string in the requested format.
    """
    title = story.get("event", "Family Story")
    members = story.get("members", "")
    style = story.get("style", "")
    created = story.get("created", "")
    content = story.get("story", "")

    if format == "html":
        html_content = content.replace("\n", "<br>\n")
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Georgia, serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.8; color: #333; }}
        .header {{ text-align: center; border-bottom: 2px solid #8B4513; padding-bottom: 1rem; margin-bottom: 2rem; }}
        .meta {{ color: #666; font-size: 0.9rem; }}
        .content {{ text-align: justify; }}
        .footer {{ text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ccc; color: #999; font-size: 0.8rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p class="meta">Family Members: {members} | Style: {style}</p>
        <p class="meta">Created: {created}</p>
    </div>
    <div class="content">
        {html_content}
    </div>
    <div class="footer">
        <p>Created with Family Story Creator v2.0.0</p>
    </div>
</body>
</html>"""

    # Default: markdown
    return f"""# {title}

> **Family Members**: {members}
> **Style**: {style}
> **Created**: {created}

---

{content}

---

*Created with Family Story Creator v2.0.0*
"""
