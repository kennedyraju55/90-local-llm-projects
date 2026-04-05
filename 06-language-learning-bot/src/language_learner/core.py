"""Core business logic for Language Learning Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
from datetime import datetime

from .config import load_config
from .utils import get_llm_client, load_json_file, save_json_file, get_data_path

logger = logging.getLogger(__name__)

chat, check_ollama_running = get_llm_client()

SYSTEM_PROMPT_TEMPLATE = """You are a friendly and patient {language} language tutor. The student is at {level} level.

Your role is to:
1. Conduct conversations in {language}, adjusting complexity to the student's level
2. Correct grammar and vocabulary mistakes gently
3. Provide translations when asked
4. Explain grammar rules when relevant
5. Suggest better ways to express ideas
6. Use encouraging language

Format your responses like this:
- First, respond naturally in {language}
- Then provide an English translation in parentheses
- If the student made mistakes, list corrections with explanations
- Suggest vocabulary or phrases the student could learn

For beginners: Use simple words, short sentences, and always provide translations.
For intermediate: Mix the target language with English explanations.
For advanced: Primarily use {language}, only explain complex grammar in English."""

LANGUAGES = [
    "spanish", "french", "german", "italian", "portuguese",
    "japanese", "korean", "chinese", "arabic", "hindi",
    "russian", "dutch", "swedish", "turkish", "greek",
]

LEVELS = ["beginner", "intermediate", "advanced"]


def get_system_prompt(language: str, level: str) -> str:
    """Build the system prompt for the specified language and level."""
    return SYSTEM_PROMPT_TEMPLATE.format(language=language.capitalize(), level=level)


def get_response(user_message: str, history: list[dict], language: str, level: str) -> str:
    """Get a response from the language tutor."""
    system_prompt = get_system_prompt(language, level)
    messages = history + [{"role": "user", "content": user_message}]
    return chat(messages, system_prompt=system_prompt)


def get_lesson(topic: str, language: str, level: str) -> str:
    """Get a mini lesson on a specific topic."""
    system_prompt = get_system_prompt(language, level)
    messages = [
        {
            "role": "user",
            "content": (
                f"Give me a short {language} lesson about: {topic}\n"
                "Include: key vocabulary (with pronunciation), example sentences, "
                "grammar notes, and a practice exercise."
            ),
        }
    ]
    return chat(messages, system_prompt=system_prompt, max_tokens=2048)


def get_pronunciation_tips(word: str, language: str) -> str:
    """Get pronunciation tips for a word in the target language."""
    system_prompt = get_system_prompt(language, "beginner")
    messages = [
        {
            "role": "user",
            "content": (
                f"Give me detailed pronunciation tips for the {language} word/phrase: '{word}'\n"
                "Include: phonetic breakdown, common mistakes, mouth position tips, "
                "and similar-sounding words in English."
            ),
        }
    ]
    return chat(messages, system_prompt=system_prompt, max_tokens=1024)


def generate_lesson_plan(language: str, level: str, duration_weeks: int = 4) -> str:
    """Generate a structured lesson plan."""
    system_prompt = get_system_prompt(language, level)
    messages = [
        {
            "role": "user",
            "content": (
                f"Create a {duration_weeks}-week lesson plan for learning {language} at {level} level.\n"
                "Include:\n"
                "- Weekly themes and topics\n"
                "- Daily practice activities (15-30 min each)\n"
                "- Vocabulary goals per week\n"
                "- Grammar points to cover\n"
                "- Cultural notes and tips\n"
                "- Milestone assessments"
            ),
        }
    ]
    return chat(messages, system_prompt=system_prompt, max_tokens=3072)


# --- Vocabulary Tracker ---

def load_vocabulary(language: str) -> list[dict]:
    """Load vocabulary list for a language."""
    path = get_data_path(f"vocabulary_{language}.json")
    data = load_json_file(path)
    return data if isinstance(data, list) else []


def save_vocabulary(language: str, vocab: list[dict]) -> None:
    """Save vocabulary list for a language."""
    path = get_data_path(f"vocabulary_{language}.json")
    save_json_file(path, vocab)


def add_vocabulary_word(language: str, word: str, translation: str,
                        example: str = "", notes: str = "") -> dict:
    """Add a word to the vocabulary tracker."""
    vocab = load_vocabulary(language)
    entry = {
        "id": len(vocab) + 1,
        "word": word,
        "translation": translation,
        "example": example,
        "notes": notes,
        "added_date": datetime.now().isoformat(),
        "review_count": 0,
        "mastered": False,
    }
    vocab.append(entry)
    save_vocabulary(language, vocab)
    logger.info("Added vocabulary: %s -> %s", word, translation)
    return entry


def get_vocabulary_quiz(language: str, count: int = 5) -> str:
    """Generate a vocabulary quiz from saved words."""
    vocab = load_vocabulary(language)
    if not vocab:
        return "No vocabulary words saved yet. Add some words first!"
    words_text = "\n".join(
        f"- {w['word']} ({w['translation']})" for w in vocab[-20:]
    )
    system_prompt = get_system_prompt(language, "beginner")
    messages = [
        {
            "role": "user",
            "content": (
                f"Create a {count}-question quiz using these {language} vocabulary words:\n"
                f"{words_text}\n\n"
                "Mix question types: fill-in-the-blank, translation, and usage in sentences."
            ),
        }
    ]
    return chat(messages, system_prompt=system_prompt, max_tokens=2048)


# --- Progress Tracking ---

def load_progress(language: str) -> dict:
    """Load learning progress for a language."""
    path = get_data_path(f"progress_{language}.json")
    data = load_json_file(path)
    if isinstance(data, dict):
        return data
    return {
        "language": language,
        "sessions": [],
        "total_time_minutes": 0,
        "lessons_completed": 0,
        "words_learned": 0,
    }


def save_progress(language: str, progress: dict) -> None:
    """Save learning progress."""
    path = get_data_path(f"progress_{language}.json")
    save_json_file(path, progress)


def record_session(language: str, level: str, duration_minutes: int,
                   topic: str = "conversation") -> dict:
    """Record a learning session."""
    progress = load_progress(language)
    session = {
        "date": datetime.now().isoformat(),
        "level": level,
        "duration_minutes": duration_minutes,
        "topic": topic,
    }
    progress.setdefault("sessions", []).append(session)
    progress["total_time_minutes"] = progress.get("total_time_minutes", 0) + duration_minutes
    save_progress(language, progress)
    logger.info("Recorded %d-min session for %s", duration_minutes, language)
    return session


def get_progress_summary(language: str) -> str:
    """Get a formatted progress summary."""
    progress = load_progress(language)
    sessions = progress.get("sessions", [])
    if not sessions:
        return f"No sessions recorded for {language.capitalize()} yet."
    total = progress.get("total_time_minutes", 0)
    vocab_count = len(load_vocabulary(language))
    hours = total // 60
    mins = total % 60
    return (
        f"📊 {language.capitalize()} Progress\n"
        f"  Sessions: {len(sessions)}\n"
        f"  Total Time: {hours}h {mins}m\n"
        f"  Vocabulary: {vocab_count} words\n"
        f"  Last Session: {sessions[-1]['date'][:10]}"
    )
