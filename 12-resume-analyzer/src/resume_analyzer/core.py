"""Core business logic for Resume Analyzer."""

import json
import logging
from typing import Any

from .config import load_config
from .utils import get_llm_client, parse_json_response

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an expert resume reviewer and career coach with 20 years of "
    "experience in HR, recruiting, and talent acquisition across multiple "
    "industries. Provide specific, actionable, and professional feedback."
)


def analyze_resume(resume_text: str, config: dict | None = None) -> dict:
    """Perform a general analysis of a resume.

    Returns dict with: skills, experience_summary, education, achievements,
    strengths, weaknesses, formatting_suggestions, content_suggestions, overall_score.
    """
    cfg = config or load_config()
    _, generate, _ = get_llm_client()

    prompt = f"""Analyze the following resume and provide a detailed evaluation.
Return your analysis as valid JSON with exactly these keys:
- "skills": list of extracted skills
- "experience_summary": brief summary of work experience
- "education": list of education entries
- "achievements": list of notable achievements
- "strengths": list of resume strengths
- "weaknesses": list of resume weaknesses
- "formatting_suggestions": list of formatting improvements
- "content_suggestions": list of content improvements
- "overall_score": integer from 0-100 rating the resume quality

IMPORTANT: Return ONLY valid JSON, no markdown fences, no extra text.

Resume:
\"\"\"
{resume_text}
\"\"\""""

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )
    return parse_json_response(response)


def score_against_jd(resume_text: str, jd_text: str, config: dict | None = None) -> dict:
    """Score a resume against a specific job description.

    Returns dict with: match_percentage, matching_skills, missing_skills,
    experience_alignment, suggestions, keyword_gaps, overall_assessment,
    priority_improvements.
    """
    cfg = config or load_config()
    _, generate, _ = get_llm_client()

    prompt = f"""Compare the following resume against the job description and evaluate the match.
Return your analysis as valid JSON with exactly these keys:
- "match_percentage": integer from 0-100 representing overall match
- "matching_skills": list of skills from the JD found in the resume
- "missing_skills": list of skills from the JD NOT found in the resume
- "experience_alignment": string describing how well experience aligns
- "suggestions": list of specific suggestions to improve the match
- "keyword_gaps": list of important keywords from JD missing in resume
- "overall_assessment": string with overall assessment paragraph
- "priority_improvements": list of top 3 most impactful changes to make

IMPORTANT: Return ONLY valid JSON, no markdown fences, no extra text.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{jd_text}
\"\"\""""

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )
    return parse_json_response(response)


def simulate_ats_score(resume_text: str, jd_text: str, config: dict | None = None) -> dict:
    """Simulate an ATS (Applicant Tracking System) score.

    Returns dict with category scores and overall ATS score.
    """
    cfg = config or load_config()
    _, generate, _ = get_llm_client()

    prompt = f"""Simulate an Applicant Tracking System (ATS) evaluation of this resume against the job description.

Return your analysis as valid JSON with these keys:
- "ats_score": integer 0-100, overall ATS compatibility score
- "keyword_match_score": integer 0-100, how well keywords match
- "experience_match_score": integer 0-100, experience relevance
- "education_match_score": integer 0-100, education relevance
- "formatting_score": integer 0-100, ATS-friendly formatting
- "matched_keywords": list of matched keywords
- "missing_keywords": list of important missing keywords
- "formatting_issues": list of ATS formatting problems
- "recommendations": list of specific changes to improve ATS score

IMPORTANT: Return ONLY valid JSON.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{jd_text}
\"\"\""""

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )
    return parse_json_response(response)


def compare_resumes(resume_texts: list[tuple[str, str]], jd_text: str | None = None,
                    config: dict | None = None) -> dict:
    """Compare multiple resumes, optionally against a job description.

    Args:
        resume_texts: List of (name, text) tuples.
        jd_text: Optional job description for ranking.
        config: Optional configuration.

    Returns:
        Comparison analysis dict.
    """
    cfg = config or load_config()
    _, generate, _ = get_llm_client()

    resumes_section = ""
    for i, (name, text) in enumerate(resume_texts, 1):
        resumes_section += f"\n--- RESUME {i}: {name} ---\n{text}\n--- END RESUME {i} ---\n"

    jd_section = ""
    if jd_text:
        jd_section = f"\nJob Description:\n\"\"\"\n{jd_text}\n\"\"\"\n"

    prompt = f"""Compare the following {len(resume_texts)} resumes{' against the job description' if jd_text else ''}.

Return your analysis as valid JSON with these keys:
- "ranking": list of objects with "name", "score" (0-100), "summary"
- "comparison_table": list of objects with "category", and one key per resume name
- "recommendation": string with overall recommendation
- "key_differences": list of major differences between candidates

IMPORTANT: Return ONLY valid JSON.

{resumes_section}
{jd_section}"""

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )
    return parse_json_response(response)


def generate_improvement_suggestions(resume_text: str, config: dict | None = None) -> dict:
    """Generate detailed improvement suggestions for a resume.

    Returns dict with section-by-section improvement suggestions.
    """
    cfg = config or load_config()
    _, generate, _ = get_llm_client()

    prompt = f"""Provide detailed, section-by-section improvement suggestions for this resume.

Return your analysis as valid JSON with these keys:
- "summary_section": object with "current_assessment", "suggestions" list
- "experience_section": object with "current_assessment", "suggestions" list
- "skills_section": object with "current_assessment", "suggestions" list
- "education_section": object with "current_assessment", "suggestions" list
- "overall_suggestions": list of general improvements
- "power_words_to_add": list of impactful action verbs to use
- "sections_to_add": list of recommended additional sections

IMPORTANT: Return ONLY valid JSON.

Resume:
\"\"\"
{resume_text}
\"\"\""""

    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )
    return parse_json_response(response)
