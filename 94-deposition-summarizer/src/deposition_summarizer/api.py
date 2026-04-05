"""FastAPI REST API for Deposition Summarizer."""

import os
import sys
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from common.llm_client import check_ollama_running

from src.deposition_summarizer.core import (
    summarize_deposition,
    find_admissions,
    find_contradictions,
    extract_testimony,
    generate_follow_up_questions,
    build_timeline,
)

app = FastAPI(
    title="Deposition Summarizer API",
    description=(
        "REST API for AI-powered deposition transcript analysis. "
        "Powered by local Gemma 4 LLM via Ollama — 100% private, zero data leakage."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# ---------------------------------------------------------------------------
# Request / Response Models
# ---------------------------------------------------------------------------

class TranscriptRequest(BaseModel):
    """Base request containing a deposition transcript."""
    transcript: str = Field(..., description="The deposition transcript text")
    model: str = Field(default="gemma4:latest", description="LLM model name")


class TestimonyRequest(TranscriptRequest):
    """Request to extract testimony on a specific topic."""
    topic: str = Field(..., description="Topic to search for in testimony")


class AdmissionResponse(BaseModel):
    """A key admission found in the transcript."""
    speaker: str
    statement: str
    page_line: str
    significance: str


class ContradictionResponse(BaseModel):
    """A contradiction detected in the transcript."""
    statement_a: str
    statement_b: str
    page_line_a: str
    page_line_b: str
    explanation: str


class TestimonyResponse(BaseModel):
    """An important piece of testimony."""
    speaker: str
    topic: str
    summary: str
    page_line: str
    relevance: str


class TimelineEventResponse(BaseModel):
    """A timeline event extracted from the transcript."""
    date: str
    event: str


class WitnessProfileResponse(BaseModel):
    """Witness profile information."""
    name: str
    role: str
    credibility_notes: List[str]
    demeanor_notes: List[str]


class SummaryResponse(BaseModel):
    """Full deposition summary response."""
    title: str
    witness: str
    date: str
    duration: str
    overall_summary: str
    key_admissions: List[AdmissionResponse]
    contradictions: List[ContradictionResponse]
    important_testimony: List[TestimonyResponse]
    witness_profile: WitnessProfileResponse
    topics_covered: List[str]
    follow_up_questions: List[str]
    timeline: List[TimelineEventResponse]
    status: str = "success"


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    ollama_ok = check_ollama_running()
    return {
        "status": "healthy" if ollama_ok else "degraded",
        "ollama": "connected" if ollama_ok else "disconnected",
        "model": "gemma4:latest",
        "service": "deposition-summarizer",
    }


@app.post("/summarize", response_model=SummaryResponse)
async def summarize_endpoint(request: TranscriptRequest):
    """Generate a comprehensive deposition summary."""
    try:
        summary = summarize_deposition(request.transcript, request.model)
        return SummaryResponse(
            title=summary.title,
            witness=summary.witness,
            date=summary.date,
            duration=summary.duration,
            overall_summary=summary.overall_summary,
            key_admissions=[
                AdmissionResponse(
                    speaker=a.speaker, statement=a.statement,
                    page_line=a.page_line, significance=a.significance,
                )
                for a in summary.key_admissions
            ],
            contradictions=[
                ContradictionResponse(
                    statement_a=c.statement_a, statement_b=c.statement_b,
                    page_line_a=c.page_line_a, page_line_b=c.page_line_b,
                    explanation=c.explanation,
                )
                for c in summary.contradictions
            ],
            important_testimony=[
                TestimonyResponse(
                    speaker=t.speaker, topic=t.topic, summary=t.summary,
                    page_line=t.page_line, relevance=t.relevance,
                )
                for t in summary.important_testimony
            ],
            witness_profile=WitnessProfileResponse(
                name=summary.witness_profile.name,
                role=summary.witness_profile.role,
                credibility_notes=summary.witness_profile.credibility_notes,
                demeanor_notes=summary.witness_profile.demeanor_notes,
            ),
            topics_covered=summary.topics_covered,
            follow_up_questions=summary.follow_up_questions,
            timeline=[
                TimelineEventResponse(date=e.get("date", ""), event=e.get("event", ""))
                for e in summary.timeline
            ],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/admissions")
async def admissions_endpoint(request: TranscriptRequest):
    """Extract key admissions from a deposition transcript."""
    try:
        results = find_admissions(request.transcript, request.model)
        return {
            "admissions": [
                {
                    "speaker": a.speaker,
                    "statement": a.statement,
                    "page_line": a.page_line,
                    "significance": a.significance,
                }
                for a in results
            ],
            "count": len(results),
            "status": "success",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/contradictions")
async def contradictions_endpoint(request: TranscriptRequest):
    """Find contradictions in a deposition transcript."""
    try:
        results = find_contradictions(request.transcript, request.model)
        return {
            "contradictions": [
                {
                    "statement_a": c.statement_a,
                    "statement_b": c.statement_b,
                    "page_line_a": c.page_line_a,
                    "page_line_b": c.page_line_b,
                    "explanation": c.explanation,
                }
                for c in results
            ],
            "count": len(results),
            "status": "success",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/testimony")
async def testimony_endpoint(request: TestimonyRequest):
    """Extract testimony on a specific topic."""
    try:
        results = extract_testimony(request.transcript, request.topic, request.model)
        return {
            "testimony": [
                {
                    "speaker": t.speaker,
                    "topic": t.topic,
                    "summary": t.summary,
                    "page_line": t.page_line,
                    "relevance": t.relevance,
                }
                for t in results
            ],
            "count": len(results),
            "status": "success",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/follow-up")
async def follow_up_endpoint(request: TranscriptRequest):
    """Generate follow-up questions for a deposition."""
    try:
        questions = generate_follow_up_questions(request.transcript, request.model)
        return {
            "questions": questions,
            "count": len(questions),
            "status": "success",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/timeline")
async def timeline_endpoint(request: TranscriptRequest):
    """Extract a chronological timeline from a deposition."""
    try:
        events = build_timeline(request.transcript, request.model)
        return {
            "timeline": events,
            "count": len(events),
            "status": "success",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
