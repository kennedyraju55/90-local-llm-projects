"""Core business logic for Study Buddy Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
from datetime import datetime

from .config import load_config
from .utils import get_llm_client, load_json_file, save_json_file, get_data_path

logger = logging.getLogger(__name__)

chat, check_ollama_running = get_llm_client()

SYSTEM_PROMPT = """You are an expert academic tutor and study coach. Your role is to:
1. Explain complex concepts in clear, simple terms
2. Create practice questions and quizzes
3. Generate study plans and revision schedules
4. Use analogies and examples to aid understanding
5. Adapt explanations to the student's level

Teaching approach:
- Break down complex topics into digestible parts
- Use the Feynman technique (explain like teaching someone else)
- Include mnemonics and memory aids when helpful
- Provide practice problems with detailed solutions
- Encourage active recall and spaced repetition"""

MODES = {
    "quiz": "Generate quiz questions to test knowledge",
    "explain": "Explain a concept in detail",
    "plan": "Create a study plan",
    "summarize": "Summarize key points of a topic",
    "flashcards": "Generate flashcard-style Q&A pairs",
}


def generate_quiz(subject: str, topic: str, num_questions: int = 5) -> str:
    """Generate quiz questions on a topic."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Create a quiz with {num_questions} questions about {topic} "
                f"in {subject}.\n"
                "Include a mix of:\n"
                "- Multiple choice questions (with 4 options)\n"
                "- True/False questions\n"
                "- Short answer questions\n\n"
                "Provide the answer key at the end with brief explanations."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=3072)


def explain_concept(subject: str, topic: str, depth: str = "detailed") -> str:
    """Explain a concept in detail."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Explain {topic} in {subject} at a {depth} level.\n"
                "Include:\n"
                "- Definition and key concepts\n"
                "- Real-world examples and analogies\n"
                "- Common misconceptions\n"
                "- Key formulas or rules (if applicable)\n"
                "- How it connects to related topics"
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=3072)


def create_study_plan(subject: str, topic: str, days: int = 7) -> str:
    """Create a study plan for exam preparation."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Create a {days}-day study plan for {topic} in {subject}.\n"
                "Include:\n"
                "- Daily study goals and time estimates\n"
                "- Specific subtopics to cover each day\n"
                "- Practice exercises and review sessions\n"
                "- Tips for effective studying\n"
                "- A final review strategy"
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=3072)


def generate_flashcards(subject: str, topic: str, count: int = 10) -> str:
    """Generate flashcard-style Q&A pairs."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Create {count} flashcards for {topic} in {subject}.\n"
                "Format each as:\n"
                "**Q:** [question]\n"
                "**A:** [concise answer]\n\n"
                "Cover the most important concepts."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=2048)


def ask_question(subject: str, topic: str, question: str, history: list[dict]) -> str:
    """Answer a study question with context."""
    full_question = f"Subject: {subject}, Topic: {topic}\nQuestion: {question}"
    messages = history + [{"role": "user", "content": full_question}]
    return chat(messages, system_prompt=SYSTEM_PROMPT)


# --- Flashcard Storage ---

def load_saved_flashcards() -> dict:
    """Load saved flashcards."""
    path = get_data_path("flashcards.json")
    data = load_json_file(path)
    return data if isinstance(data, dict) else {}


def save_flashcards_data(flashcards: dict) -> None:
    """Save flashcards."""
    path = get_data_path("flashcards.json")
    save_json_file(path, flashcards)


def save_flashcard_set(subject: str, topic: str, cards: list[dict]) -> None:
    """Save a set of flashcards."""
    flashcards = load_saved_flashcards()
    key = f"{subject}_{topic}".lower().replace(" ", "_")
    flashcards[key] = {
        "subject": subject,
        "topic": topic,
        "cards": cards,
        "created_date": datetime.now().isoformat(),
        "review_count": 0,
    }
    save_flashcards_data(flashcards)
    logger.info("Saved %d flashcards for %s - %s", len(cards), subject, topic)


def get_flashcard_set(subject: str, topic: str) -> dict | None:
    """Get a flashcard set."""
    flashcards = load_saved_flashcards()
    key = f"{subject}_{topic}".lower().replace(" ", "_")
    return flashcards.get(key)


# --- Progress Tracking ---

def load_study_progress() -> dict:
    """Load study progress."""
    path = get_data_path("study_progress.json")
    data = load_json_file(path)
    return data if isinstance(data, dict) else {"sessions": [], "subjects": {}}


def save_study_progress(progress: dict) -> None:
    """Save study progress."""
    path = get_data_path("study_progress.json")
    save_json_file(path, progress)


def record_study_session(subject: str, topic: str, mode: str,
                         duration_minutes: int) -> dict:
    """Record a study session."""
    progress = load_study_progress()
    session = {
        "date": datetime.now().isoformat(),
        "subject": subject,
        "topic": topic,
        "mode": mode,
        "duration_minutes": duration_minutes,
    }
    progress.setdefault("sessions", []).append(session)

    # Update subject stats
    subj_key = subject.lower()
    if subj_key not in progress.setdefault("subjects", {}):
        progress["subjects"][subj_key] = {"total_minutes": 0, "session_count": 0, "topics": []}
    progress["subjects"][subj_key]["total_minutes"] += duration_minutes
    progress["subjects"][subj_key]["session_count"] += 1
    if topic not in progress["subjects"][subj_key]["topics"]:
        progress["subjects"][subj_key]["topics"].append(topic)

    save_study_progress(progress)
    logger.info("Recorded study session: %s - %s (%d min)", subject, topic, duration_minutes)
    return session


def get_study_stats() -> dict:
    """Get overall study statistics."""
    progress = load_study_progress()
    sessions = progress.get("sessions", [])
    total_min = sum(s.get("duration_minutes", 0) for s in sessions)
    return {
        "total_sessions": len(sessions),
        "total_minutes": total_min,
        "total_hours": round(total_min / 60, 1),
        "subjects": progress.get("subjects", {}),
    }
