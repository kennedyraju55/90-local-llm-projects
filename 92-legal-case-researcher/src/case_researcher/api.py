"""FastAPI REST API for Legal Case Researcher.

Provides HTTP endpoints for legal research tasks.
All processing happens locally — no data leaves the machine.
"""

import os
import sys
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from common.llm_client import check_ollama_running
from src.case_researcher.core import (
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
    LEGAL_DISCLAIMER,
    SAMPLE_SCENARIOS,
)

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Legal Case Researcher API",
    description=(
        "⚖️ AI-powered legal case research API.\n\n"
        "All processing happens locally using Gemma 4 via Ollama. "
        "No data ever leaves your machine.\n\n"
        f"**{LEGAL_DISCLAIMER}**"
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class ResearchRequest(BaseModel):
    query: str = Field(..., description="Legal research question")
    jurisdiction: str = Field("federal", description="Jurisdiction filter")
    model: str = Field("gemma4:latest", description="Ollama model to use")

class CaseReferenceResponse(BaseModel):
    case_name: str = ""
    citation: str = ""
    year: str = ""
    court: str = ""
    jurisdiction: str = ""
    relevance: str = ""
    key_holding: str = ""

class ResearchResponse(BaseModel):
    query: str = ""
    jurisdiction: str = ""
    summary: str = ""
    relevant_cases: List[CaseReferenceResponse] = []
    key_legal_principles: List[str] = []
    suggested_search_terms: List[str] = []
    analysis: str = ""
    disclaimer: str = LEGAL_DISCLAIMER

class PrecedentRequest(BaseModel):
    case_facts: str = Field(..., description="Description of case facts")
    legal_issue: str = Field(..., description="The legal issue to research")
    model: str = Field("gemma4:latest", description="Ollama model to use")

class PrecedentResponse(BaseModel):
    case_name: str = ""
    citation: str = ""
    relevance_score: float = 0.0
    factual_similarity: str = ""
    legal_similarity: str = ""
    distinguishing_factors: List[str] = []
    applicable_holdings: List[str] = []
    recommendation: str = ""

class AnalyzeRequest(BaseModel):
    argument: str = Field(..., description="Legal argument text to analyze")
    model: str = Field("gemma4:latest", description="Ollama model to use")

class AnalyzeResponse(BaseModel):
    argument_summary: str = ""
    strength: str = "moderate"
    supporting_points: List[str] = []
    weaknesses: List[str] = []
    counter_arguments: List[str] = []
    suggested_improvements: List[str] = []
    relevant_doctrines: List[str] = []
    confidence_score: float = 0.0
    disclaimer: str = LEGAL_DISCLAIMER

class CitationsRequest(BaseModel):
    text: str = Field(..., description="Text containing legal citations")
    model: str = Field("gemma4:latest", description="Ollama model to use")

class SummarizeRequest(BaseModel):
    case_text: str = Field(..., description="Full text of a legal case")
    model: str = Field("gemma4:latest", description="Ollama model to use")

class HealthResponse(BaseModel):
    status: str
    ollama_running: bool
    version: str

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    """Check API and Ollama health status."""
    ollama_ok = check_ollama_running()
    return HealthResponse(
        status="healthy" if ollama_ok else "degraded",
        ollama_running=ollama_ok,
        version="1.0.0",
    )


@app.post("/research", response_model=ResearchResponse, tags=["Research"])
async def api_research(req: ResearchRequest):
    """Research case law for a given legal question."""
    if not check_ollama_running():
        raise HTTPException(status_code=503, detail="Ollama is not running. Start it with: ollama serve")
    try:
        result = research_case_law(req.query, jurisdiction=req.jurisdiction, model=req.model)
        return ResearchResponse(
            query=result.query,
            jurisdiction=result.jurisdiction,
            summary=result.summary,
            relevant_cases=[
                CaseReferenceResponse(
                    case_name=c.case_name,
                    citation=c.citation,
                    year=c.year,
                    court=c.court,
                    jurisdiction=c.jurisdiction,
                    relevance=c.relevance,
                    key_holding=c.key_holding,
                )
                for c in result.relevant_cases
            ],
            key_legal_principles=result.key_legal_principles,
            suggested_search_terms=result.suggested_search_terms,
            analysis=result.analysis,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/precedents", response_model=List[PrecedentResponse], tags=["Research"])
async def api_precedents(req: PrecedentRequest):
    """Find relevant legal precedents for given case facts."""
    if not check_ollama_running():
        raise HTTPException(status_code=503, detail="Ollama is not running. Start it with: ollama serve")
    try:
        results = find_precedents(req.case_facts, req.legal_issue, model=req.model)
        return [
            PrecedentResponse(
                case_name=p.case_name,
                citation=p.citation,
                relevance_score=p.relevance_score,
                factual_similarity=p.factual_similarity,
                legal_similarity=p.legal_similarity,
                distinguishing_factors=p.distinguishing_factors,
                applicable_holdings=p.applicable_holdings,
                recommendation=p.recommendation,
            )
            for p in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze", response_model=AnalyzeResponse, tags=["Analysis"])
async def api_analyze(req: AnalyzeRequest):
    """Analyze the strength of a legal argument."""
    if not check_ollama_running():
        raise HTTPException(status_code=503, detail="Ollama is not running. Start it with: ollama serve")
    try:
        result = analyze_legal_argument(req.argument, model=req.model)
        return AnalyzeResponse(
            argument_summary=result.argument_summary,
            strength=result.strength,
            supporting_points=result.supporting_points,
            weaknesses=result.weaknesses,
            counter_arguments=result.counter_arguments,
            suggested_improvements=result.suggested_improvements,
            relevant_doctrines=result.relevant_doctrines,
            confidence_score=result.confidence_score,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/citations", response_model=List[CaseReferenceResponse], tags=["Extraction"])
async def api_citations(req: CitationsRequest):
    """Extract legal case citations from text."""
    if not check_ollama_running():
        raise HTTPException(status_code=503, detail="Ollama is not running. Start it with: ollama serve")
    try:
        results = extract_citations(req.text, model=req.model)
        return [
            CaseReferenceResponse(
                case_name=c.case_name,
                citation=c.citation,
                year=c.year,
                court=c.court,
                jurisdiction=c.jurisdiction,
                relevance=c.relevance,
                key_holding=c.key_holding,
            )
            for c in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize", tags=["Analysis"])
async def api_summarize(req: SummarizeRequest):
    """Summarize a legal case document."""
    if not check_ollama_running():
        raise HTTPException(status_code=503, detail="Ollama is not running. Start it with: ollama serve")
    try:
        result = summarize_case(req.case_text, model=req.model)
        result["disclaimer"] = LEGAL_DISCLAIMER
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/samples", tags=["Reference"])
async def api_samples():
    """Get sample legal research scenarios."""
    return {
        "scenarios": SAMPLE_SCENARIOS,
        "disclaimer": LEGAL_DISCLAIMER,
    }
