"""Core business logic for Newsletter Editor."""

import logging
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

logger = logging.getLogger(__name__)

# ── Default Configuration ────────────────────────────────────────────
DEFAULT_CONFIG = {
    "llm": {
        "temperature": 0.7,
        "max_tokens": 4096,
    },
    "newsletter": {
        "default_sections": 4,
        "default_tone": "informative",
        "supported_tones": ["informative", "casual", "witty", "formal", "friendly"],
    },
    "export": {
        "output_dir": "output",
        "archive_dir": "archive",
    },
}

# ── Section Templates ────────────────────────────────────────────────
SECTION_TEMPLATES = {
    "news_roundup": {
        "name": "News Roundup",
        "description": "Collection of top news items with brief summaries",
        "prompt_hint": "Format as a numbered list with headline and 1-2 sentence summary each.",
    },
    "deep_dive": {
        "name": "Deep Dive",
        "description": "In-depth analysis of a single topic",
        "prompt_hint": "Provide thorough analysis with data points, expert quotes, and actionable insights.",
    },
    "tips_tricks": {
        "name": "Tips & Tricks",
        "description": "Quick actionable tips for the reader",
        "prompt_hint": "Format as short, actionable bullet points readers can implement immediately.",
    },
    "spotlight": {
        "name": "Spotlight",
        "description": "Feature a person, tool, or resource",
        "prompt_hint": "Write a mini-profile highlighting key achievements or features.",
    },
    "upcoming_events": {
        "name": "Upcoming Events",
        "description": "List of relevant upcoming events or deadlines",
        "prompt_hint": "Format as a timeline with dates, event names, and brief descriptions.",
    },
    "reader_qa": {
        "name": "Reader Q&A",
        "description": "Answer reader-submitted questions",
        "prompt_hint": "Format as Q&A pairs with clear, helpful answers.",
    },
}

# ── Subscriber Segments ──────────────────────────────────────────────
SUBSCRIBER_SEGMENTS = {
    "all": {"name": "All Subscribers", "description": "Full newsletter for all subscribers"},
    "new": {"name": "New Subscribers", "description": "Include welcome message and onboarding content"},
    "premium": {"name": "Premium", "description": "Include exclusive deep-dive and premium resources"},
    "inactive": {"name": "Re-engagement", "description": "Include highlights and re-engagement hooks"},
}


def load_config(config_path: Optional[str] = None) -> dict:
    """Load configuration from YAML file with defaults."""
    config = DEFAULT_CONFIG.copy()
    if config_path and os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            user_config = yaml.safe_load(f) or {}
        _deep_merge(config, user_config)
        logger.info("Loaded config from %s", config_path)
    return config


def _deep_merge(base: dict, override: dict) -> None:
    """Deep merge override dict into base dict."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value


def read_input_file(filepath: str) -> str:
    """Read raw notes/content from a file."""
    path = Path(filepath)
    if not path.exists():
        logger.error("File not found: %s", filepath)
        raise FileNotFoundError(f"Input file not found: {filepath}")
    content = path.read_text(encoding="utf-8")
    logger.info("Read %d chars from %s", len(content), filepath)
    return content


def get_section_templates() -> dict:
    """Return available section templates."""
    return SECTION_TEMPLATES


def get_subscriber_segments() -> dict:
    """Return available subscriber segments."""
    return SUBSCRIBER_SEGMENTS


def build_prompt(
    raw_content: str,
    name: str,
    sections: int,
    tone: str,
    template: Optional[str] = None,
    segment: Optional[str] = None,
) -> str:
    """Build the newsletter generation prompt."""
    template_hint = ""
    if template and template in SECTION_TEMPLATES:
        t = SECTION_TEMPLATES[template]
        template_hint = f"\nSection Template: {t['name']}\nTemplate Guidance: {t['prompt_hint']}\n"

    segment_hint = ""
    if segment and segment in SUBSCRIBER_SEGMENTS:
        s = SUBSCRIBER_SEGMENTS[segment]
        segment_hint = f"\nTarget Audience Segment: {s['name']}\nSegment Note: {s['description']}\n"

    return (
        f"Transform the following raw notes into a polished, professional newsletter.\n\n"
        f"Newsletter Name: {name}\n"
        f"Number of Sections: {sections}\n"
        f"Tone: {tone}\n"
        f"{template_hint}{segment_hint}\n"
        f"Raw Notes/Content:\n---\n{raw_content}\n---\n\n"
        f"Requirements:\n"
        f"1. Create a compelling newsletter header with the name and a tagline\n"
        f"2. Write an engaging editorial intro (2-3 sentences)\n"
        f"3. Organize the content into {sections} distinct sections with:\n"
        f"   - Section title (catchy and descriptive)\n"
        f"   - Rewritten content (clear, concise, engaging)\n"
        f"   - Key takeaway or action item for each section\n"
        f"4. Add a brief closing/sign-off\n"
        f"5. Use markdown formatting throughout\n"
        f"6. Add relevant emoji for visual appeal\n"
        f"7. If the raw notes mention links/URLs, preserve them\n"
    )


def generate_newsletter(
    raw_content: str,
    name: str,
    sections: int,
    tone: str,
    template: Optional[str] = None,
    segment: Optional[str] = None,
    config: Optional[dict] = None,
) -> str:
    """Generate a newsletter using the LLM."""
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    from common.llm_client import chat

    cfg = config or DEFAULT_CONFIG
    system_prompt = (
        "You are an expert newsletter editor and content curator. "
        "You transform raw, unstructured notes into polished, engaging newsletters "
        "that readers love. You have a keen eye for storytelling and information hierarchy."
    )
    user_prompt = build_prompt(raw_content, name, sections, tone, template, segment)
    messages = [{"role": "user", "content": user_prompt}]
    logger.info("Generating newsletter '%s' with %d sections, tone=%s", name, sections, tone)
    return chat(
        messages,
        system_prompt=system_prompt,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def export_to_html(markdown_content: str, newsletter_name: str) -> str:
    """Convert newsletter markdown to styled HTML."""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{newsletter_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
               max-width: 680px; margin: 0 auto; padding: 20px; color: #333; line-height: 1.6; }}
        h1 {{ color: #1a1a2e; border-bottom: 3px solid #16213e; padding-bottom: 10px; }}
        h2 {{ color: #16213e; margin-top: 30px; }}
        blockquote {{ border-left: 4px solid #0f3460; padding-left: 16px; color: #555; }}
        a {{ color: #e94560; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd;
                   font-size: 0.9em; color: #777; }}
    </style>
</head>
<body>
    <div class="content">{_md_to_html(markdown_content)}</div>
    <div class="footer">
        <p>Generated by Newsletter Editor | {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
</body>
</html>"""
    logger.info("Exported newsletter to HTML")
    return html_template


def _md_to_html(md: str) -> str:
    """Simple markdown to HTML conversion."""
    import re
    html = md
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'^\- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'((?:<li>.*</li>\n?)+)', r'<ul>\1</ul>', html)
    html = re.sub(r'\n\n', '</p><p>', html)
    html = f'<p>{html}</p>'
    return html


def archive_newsletter(content: str, name: str, config: Optional[dict] = None) -> str:
    """Archive a generated newsletter to the archive directory."""
    cfg = config or DEFAULT_CONFIG
    archive_dir = Path(cfg["export"]["archive_dir"])
    archive_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = name.lower().replace(" ", "_")
    filename = f"{safe_name}_{timestamp}.md"
    filepath = archive_dir / filename
    filepath.write_text(content, encoding="utf-8")
    logger.info("Archived newsletter to %s", filepath)
    return str(filepath)


def list_archive(config: Optional[dict] = None) -> list[dict]:
    """List archived newsletters."""
    cfg = config or DEFAULT_CONFIG
    archive_dir = Path(cfg["export"]["archive_dir"])
    if not archive_dir.exists():
        return []
    archives = []
    for f in sorted(archive_dir.glob("*.md"), reverse=True):
        stat = f.stat()
        archives.append({
            "filename": f.name,
            "path": str(f),
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        })
    return archives
