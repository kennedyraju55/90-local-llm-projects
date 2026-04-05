#!/usr/bin/env python3
"""Reading List Manager - Core functions for book management and recommendations."""

import sys
import os
import json
import logging
from datetime import datetime, date
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running

from rich.console import Console
from rich.table import Table

logger = logging.getLogger(__name__)
console = Console()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')


def load_config() -> dict:
    """Load application configuration from config.yaml."""
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r') as f:
                return yaml.safe_load(f)
        except (yaml.YAMLError, IOError) as e:
            logger.warning("Failed to load config.yaml: %s. Using defaults.", e)
    return {
        "app": {"name": "Reading List Manager", "version": "1.0.0", "log_level": "INFO", "data_dir": "./data"},
        "reading": {
            "statuses": ["to-read", "reading", "completed", "dropped", "on-hold"],
            "genres": ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery",
                       "Biography", "Self-Help", "Technical", "History", "Philosophy"],
            "max_rating": 5,
            "yearly_goal": 24,
            "pages_per_session": 30,
        },
        "llm": {"model": "llama3", "temperature": 0.6, "system_prompt": "You are a well-read literary assistant."},
    }


config = load_config()

# Configure logging from config
logging.basicConfig(
    level=getattr(logging, config.get("app", {}).get("log_level", "INFO"), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

DATA_DIR = config.get("app", {}).get("data_dir", "./data")
BOOKS_FILE = os.path.join(os.path.dirname(__file__), '..', '..', DATA_DIR, "reading_list.json")
GOALS_FILE = os.path.join(os.path.dirname(__file__), '..', '..', DATA_DIR, "reading_goals.json")

STATUS_EMOJI = {
    "to-read": "📋",
    "reading": "📖",
    "completed": "✅",
    "dropped": "❌",
    "on-hold": "⏸️",
}

# ---------------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------------


def load_books() -> dict:
    """Load reading list from JSON file."""
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error("Error loading books file: %s", e)
            return {"books": []}
    return {"books": []}


def save_books(data: dict) -> None:
    """Save reading list to JSON file."""
    os.makedirs(os.path.dirname(BOOKS_FILE), exist_ok=True)
    with open(BOOKS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    logger.info("Saved %d books to %s", len(data.get("books", [])), BOOKS_FILE)


# ---------------------------------------------------------------------------
# Book CRUD
# ---------------------------------------------------------------------------


def add_book(
    title: str,
    author: str,
    genre: str = "",
    status: str = "to-read",
    rating: int = 0,
    notes: str = "",
    pages: int = 0,
) -> dict:
    """Add a book to the reading list."""
    data = load_books()
    book = {
        "id": len(data["books"]) + 1,
        "title": title,
        "author": author,
        "genre": genre,
        "status": status,
        "rating": rating,
        "notes": notes,
        "pages": pages,
        "pages_read": 0,
        "progress_percent": 0.0,
        "review": "",
        "added": datetime.now().isoformat(),
        "started": None,
        "finished": None,
    }
    data["books"].append(book)
    save_books(data)
    logger.info("Added book: '%s' by %s", title, author)
    return book


def _find_book(data: dict, book_id: int) -> Optional[dict]:
    """Find a book by its ID. Returns None if not found."""
    for book in data["books"]:
        if book["id"] == book_id:
            return book
    return None


# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------


def update_progress(book_id: int, pages_read: int) -> Optional[dict]:
    """Track reading progress – pages read and percent complete."""
    data = load_books()
    book = _find_book(data, book_id)
    if book is None:
        logger.warning("Book with id %d not found.", book_id)
        return None

    book["pages_read"] = pages_read
    total = book.get("pages", 0)
    book["progress_percent"] = round((pages_read / total) * 100, 1) if total > 0 else 0.0

    if pages_read > 0 and book["status"] == "to-read":
        book["status"] = "reading"
        book["started"] = book.get("started") or datetime.now().isoformat()

    if total > 0 and pages_read >= total:
        book["status"] = "completed"
        book["finished"] = book.get("finished") or datetime.now().isoformat()
        book["progress_percent"] = 100.0

    save_books(data)
    logger.info("Updated progress for book %d: %d/%d pages", book_id, pages_read, total)
    return book


# ---------------------------------------------------------------------------
# Ratings & reviews
# ---------------------------------------------------------------------------


def rate_book(book_id: int, rating: int, review: str = "") -> Optional[dict]:
    """Rate a book 1-5 with an optional review."""
    if not 1 <= rating <= config.get("reading", {}).get("max_rating", 5):
        raise ValueError(f"Rating must be between 1 and {config['reading']['max_rating']}")

    data = load_books()
    book = _find_book(data, book_id)
    if book is None:
        logger.warning("Book with id %d not found.", book_id)
        return None

    book["rating"] = rating
    if review:
        book["review"] = review
    save_books(data)
    logger.info("Rated book %d: %d/5", book_id, rating)
    return book


# ---------------------------------------------------------------------------
# Genre statistics
# ---------------------------------------------------------------------------


def get_genre_stats(books: list[dict]) -> dict:
    """Compute per-genre stats: count and average rating."""
    genre_data: dict[str, dict] = defaultdict(lambda: {"count": 0, "total_rating": 0, "rated_count": 0})
    for book in books:
        genre = book.get("genre") or "Unknown"
        genre_data[genre]["count"] += 1
        r = book.get("rating", 0)
        if r and r > 0:
            genre_data[genre]["total_rating"] += r
            genre_data[genre]["rated_count"] += 1

    stats = {}
    for genre, d in genre_data.items():
        avg = round(d["total_rating"] / d["rated_count"], 2) if d["rated_count"] else 0.0
        stats[genre] = {"count": d["count"], "avg_rating": avg}
    return stats


# ---------------------------------------------------------------------------
# Pure-Python recommendation engine
# ---------------------------------------------------------------------------


def recommend_similar(books: list[dict], top_n: int = 5) -> list[dict]:
    """Recommend books from the library that are similar to highly-rated ones.

    Uses genre + rating matching. Returns books sorted by a similarity score
    relative to the reader's favourites.
    """
    if not books:
        return []

    rated = [b for b in books if b.get("rating", 0) >= 4]
    if not rated:
        rated = books

    favourite_genres: dict[str, float] = defaultdict(float)
    for b in rated:
        g = b.get("genre") or "Unknown"
        favourite_genres[g] += b.get("rating", 3)

    unread = [b for b in books if b.get("status") in ("to-read", "on-hold")]
    if not unread:
        return []

    scored: list[tuple[float, dict]] = []
    for b in unread:
        genre = b.get("genre") or "Unknown"
        score = favourite_genres.get(genre, 0)
        scored.append((score, b))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_n]]


# ---------------------------------------------------------------------------
# Reading speed
# ---------------------------------------------------------------------------


def calculate_reading_speed(book: dict) -> Optional[float]:
    """Calculate pages per day based on start/end dates and pages read."""
    started = book.get("started")
    finished = book.get("finished")
    pages = book.get("pages_read") or book.get("pages", 0)
    if not started or pages <= 0:
        return None

    start_dt = datetime.fromisoformat(started).date()
    end_dt = datetime.fromisoformat(finished).date() if finished else date.today()
    days = max((end_dt - start_dt).days, 1)
    return round(pages / days, 1)


# ---------------------------------------------------------------------------
# Reading goals
# ---------------------------------------------------------------------------


def _load_goals() -> dict:
    """Load reading goals from JSON file."""
    if os.path.exists(GOALS_FILE):
        try:
            with open(GOALS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"goals": {}}
    return {"goals": {}}


def _save_goals(data: dict) -> None:
    """Save reading goals to JSON file."""
    os.makedirs(os.path.dirname(GOALS_FILE), exist_ok=True)
    with open(GOALS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def set_reading_goal(year: int, target: int) -> dict:
    """Set a yearly reading goal."""
    goals = _load_goals()
    goals["goals"][str(year)] = {"target": target, "set_on": datetime.now().isoformat()}
    _save_goals(goals)
    logger.info("Set reading goal for %d: %d books", year, target)
    return goals["goals"][str(year)]


def check_goal_progress(year: int, books: list[dict]) -> dict:
    """Check progress toward the yearly reading goal."""
    goals = _load_goals()
    goal_entry = goals.get("goals", {}).get(str(year))
    target = goal_entry["target"] if goal_entry else config.get("reading", {}).get("yearly_goal", 24)

    completed = [
        b for b in books
        if b.get("status") == "completed"
        and b.get("finished")
        and datetime.fromisoformat(b["finished"]).year == year
    ]

    count = len(completed)
    pct = round((count / target) * 100, 1) if target > 0 else 0.0
    remaining = max(target - count, 0)

    today = date.today()
    days_left = (date(year, 12, 31) - today).days if today.year == year else 0
    pace_needed = round(remaining / max(days_left, 1) * 30, 1) if remaining > 0 and days_left > 0 else 0.0

    return {
        "year": year,
        "target": target,
        "completed": count,
        "percent": pct,
        "remaining": remaining,
        "days_left": days_left,
        "books_per_month_needed": pace_needed,
    }


# ---------------------------------------------------------------------------
# TBR management
# ---------------------------------------------------------------------------


def get_tbr_list(books: list[dict]) -> list[dict]:
    """Return the to-be-read list ordered by date added."""
    tbr = [b for b in books if b.get("status") in ("to-read", "on-hold")]
    tbr.sort(key=lambda b: b.get("added", ""))
    return tbr


def prioritize_tbr(books: list[dict], sort_by: str = "genre") -> list[dict]:
    """Prioritize TBR list. sort_by can be 'genre', 'pages', or 'added'."""
    tbr = get_tbr_list(books)
    if sort_by == "pages":
        tbr.sort(key=lambda b: b.get("pages", 0))
    elif sort_by == "genre":
        tbr.sort(key=lambda b: b.get("genre", ""))
    elif sort_by == "added":
        tbr.sort(key=lambda b: b.get("added", ""))
    return tbr


# ---------------------------------------------------------------------------
# AI-powered functions (LLM)
# ---------------------------------------------------------------------------


def get_summary(title: str, author: str) -> str:
    """Get an AI-generated book summary."""
    llm_cfg = config.get("llm", {})
    prompt = f"""Provide a comprehensive summary of the book "{title}" by {author}.

Include:
1. **Overview**: Brief synopsis (2-3 sentences)
2. **Key Themes**: Main themes explored
3. **Key Takeaways**: Most important lessons or insights
4. **Who Should Read It**: Target audience
5. **Similar Books**: 3 similar book recommendations

Format in markdown."""

    logger.info("Requesting summary for '%s' by %s", title, author)
    return generate(
        prompt=prompt,
        system_prompt=llm_cfg.get("system_prompt", "You are a well-read literary assistant who provides insightful book summaries."),
        temperature=llm_cfg.get("temperature", 0.6),
    )


def get_recommendations(genre: str = "", books: list[dict] = None) -> str:
    """Get AI book recommendations based on reading history."""
    llm_cfg = config.get("llm", {})
    books_text = ""
    if books:
        books_text = "\n".join(
            f"- \"{b['title']}\" by {b['author']} (Genre: {b.get('genre', 'N/A')}, Rating: {b.get('rating', 'N/A')}/5)"
            for b in books
        )

    prompt = f"""Based on this reading history:
{books_text or 'No reading history available.'}

{f'Genre preference: {genre}' if genre else ''}

Recommend 5 books with:
1. **Title and Author**: Full book details
2. **Why This Book**: Why it matches the reader's taste
3. **Genre**: Book category
4. **Difficulty Level**: Easy/Medium/Advanced read
5. **Key Insight**: What makes this book special

Format as a numbered list in markdown."""

    logger.info("Requesting recommendations (genre=%s)", genre)
    return generate(
        prompt=prompt,
        system_prompt="You are an expert book recommender who understands reader preferences and can suggest perfect next reads.",
        temperature=llm_cfg.get("temperature", 0.7),
    )


def analyze_reading_habits(books: list[dict]) -> str:
    """Analyze reading habits and patterns using the LLM."""
    llm_cfg = config.get("llm", {})
    books_text = json.dumps(books, indent=2)
    prompt = f"""Analyze these reading habits:

{books_text}

Provide:
1. **Reading Profile**: What kind of reader is this person?
2. **Genre Distribution**: Favorite genres and balance
3. **Rating Patterns**: What they tend to rate highly
4. **Reading Pace**: Observations about reading speed
5. **Suggestions**: How to diversify or deepen reading

Format in markdown."""

    logger.info("Requesting reading habits analysis")
    return generate(
        prompt=prompt,
        system_prompt="You are a reading habit analyst.",
        temperature=llm_cfg.get("temperature", 0.5),
    )


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------


def display_books(books: list[dict]) -> None:
    """Display reading list in a formatted table."""
    table = Table(title="📚 Reading List", show_lines=True)
    table.add_column("ID", style="cyan", width=5)
    table.add_column("Title", style="white", min_width=20)
    table.add_column("Author", style="green", min_width=15)
    table.add_column("Genre", style="blue", min_width=12)
    table.add_column("Status", style="yellow", min_width=10)
    table.add_column("Rating", style="magenta", width=8)
    table.add_column("Progress", style="cyan", width=10)

    for book in books:
        status = book.get("status", "to-read")
        emoji = STATUS_EMOJI.get(status, "📋")
        rating = "⭐" * book.get("rating", 0) if book.get("rating") else "-"
        pct = book.get("progress_percent", 0)
        progress = f"{pct:.0f}%" if pct else "-"
        table.add_row(
            str(book["id"]),
            book["title"],
            book["author"],
            book.get("genre", "-"),
            f"{emoji} {status}",
            rating,
            progress,
        )

    console.print(table)
