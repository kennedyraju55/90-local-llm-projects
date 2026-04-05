"""Core business logic for Mood Journal Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
from datetime import datetime, timedelta
from collections import Counter

from .config import load_config
from .utils import get_llm_client, load_json_file, save_json_file, get_data_path, export_to_csv

logger = logging.getLogger(__name__)

chat, check_ollama_running = get_llm_client()

SYSTEM_PROMPT = """You are an empathetic and supportive mood journal analyst. Your role is to:
1. Help users reflect on their emotions and experiences
2. Identify mood patterns and trends over time
3. Provide supportive, non-judgmental responses
4. Suggest healthy coping strategies when appropriate
5. Celebrate positive moments and progress

Guidelines:
- Be warm, empathetic, and encouraging
- Never diagnose mental health conditions
- Recommend professional help if entries suggest serious distress
- Focus on patterns, not individual entries
- Respect privacy and emotional vulnerability"""

MOODS = {
    "1": ("😊", "Happy", "green"),
    "2": ("😌", "Calm", "cyan"),
    "3": ("😐", "Neutral", "white"),
    "4": ("😔", "Sad", "blue"),
    "5": ("😤", "Angry", "red"),
    "6": ("😰", "Anxious", "yellow"),
    "7": ("😫", "Stressed", "magenta"),
    "8": ("🥰", "Grateful", "green"),
    "9": ("😴", "Tired", "dim"),
    "10": ("🤗", "Excited", "bright_yellow"),
}

JOURNAL_FILE = get_data_path("journal_entries.json")


def load_entries() -> list[dict]:
    """Load journal entries from the JSON file."""
    return load_json_file(JOURNAL_FILE) if isinstance(load_json_file(JOURNAL_FILE), list) else []


def save_entries(entries: list[dict]) -> None:
    """Save journal entries to the JSON file."""
    save_json_file(JOURNAL_FILE, entries)


def add_entry(mood_key: str, text: str, energy_level: int = 5,
              gratitude: str = "") -> dict:
    """Create and save a new journal entry."""
    emoji, mood_name, _ = MOODS[mood_key]
    entry = {
        "id": len(load_entries()) + 1,
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        "mood": mood_name,
        "mood_emoji": emoji,
        "mood_score": int(mood_key),
        "energy_level": energy_level,
        "text": text,
        "gratitude": gratitude,
    }
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)
    logger.info("Added journal entry: %s %s", emoji, mood_name)
    return entry


def get_recent_entries(days: int = 7) -> list[dict]:
    """Get entries from the last N days."""
    entries = load_entries()
    cutoff = datetime.now() - timedelta(days=days)
    return [
        e for e in entries
        if datetime.fromisoformat(e["timestamp"]) >= cutoff
    ]


def analyze_entries(entries: list[dict]) -> str:
    """Analyze mood patterns in journal entries using LLM."""
    if not entries:
        return "No entries to analyze. Start journaling to see insights!"

    summary_lines = []
    for e in entries:
        gratitude_note = f" | Grateful for: {e.get('gratitude', '')}" if e.get("gratitude") else ""
        summary_lines.append(
            f"- {e['date']} {e['time']}: {e['mood_emoji']} {e['mood']} "
            f"(energy: {e['energy_level']}/10) — {e['text'][:100]}{gratitude_note}"
        )
    entries_text = "\n".join(summary_lines)

    messages = [
        {
            "role": "user",
            "content": (
                f"Analyze these mood journal entries and provide insights:\n\n"
                f"{entries_text}\n\n"
                "Please provide:\n"
                "1. Overall mood trend (improving, declining, stable)\n"
                "2. Most common moods and potential triggers\n"
                "3. Energy level patterns\n"
                "4. Positive observations\n"
                "5. Gentle suggestions for well-being\n"
                "Be warm, supportive, and encouraging."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=2048)


def generate_weekly_report(entries: list[dict]) -> str:
    """Generate a weekly mood report."""
    if not entries:
        return "No entries for this week."

    mood_counts = Counter(e.get("mood", "Unknown") for e in entries)
    avg_energy = sum(e.get("energy_level", 5) for e in entries) / len(entries)

    summary = (
        f"📊 **Weekly Report** ({entries[0]['date']} to {entries[-1]['date']})\n\n"
        f"**Entries:** {len(entries)}\n"
        f"**Average Energy:** {avg_energy:.1f}/10\n\n"
        f"**Mood Distribution:**\n"
    )
    for mood, count in mood_counts.most_common():
        pct = (count / len(entries)) * 100
        summary += f"- {mood}: {count} ({pct:.0f}%)\n"

    return summary


def generate_monthly_report() -> str:
    """Generate a monthly mood report."""
    entries = get_recent_entries(30)
    if not entries:
        return "No entries in the last 30 days."

    report = generate_weekly_report(entries)

    # Add gratitude highlights
    grateful_entries = [e for e in entries if e.get("gratitude")]
    if grateful_entries:
        report += "\n**🙏 Gratitude Highlights:**\n"
        for e in grateful_entries[-5:]:
            report += f"- {e['date']}: {e['gratitude']}\n"

    return report


def get_gratitude_prompt() -> str:
    """Generate a gratitude prompt using LLM."""
    messages = [
        {
            "role": "user",
            "content": (
                "Generate a thoughtful gratitude prompt for journaling. "
                "Make it specific and thought-provoking, not generic. "
                "Just provide the prompt, nothing else."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=256)


def get_mood_stats() -> dict:
    """Get overall mood statistics."""
    entries = load_entries()
    if not entries:
        return {"total": 0, "mood_counts": {}, "avg_energy": 0}

    mood_counts: dict[str, int] = {}
    total_energy = 0
    for e in entries:
        mood = e.get("mood", "Unknown")
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
        total_energy += e.get("energy_level", 5)

    return {
        "total": len(entries),
        "mood_counts": mood_counts,
        "avg_energy": round(total_energy / len(entries), 1),
        "first_date": entries[0].get("date", "N/A"),
        "last_date": entries[-1].get("date", "N/A"),
    }


def export_entries(filepath: str, days: int | None = None) -> int:
    """Export entries to CSV. Returns count of exported entries."""
    if days:
        entries = get_recent_entries(days)
    else:
        entries = load_entries()
    export_to_csv(entries, filepath)
    return len(entries)
