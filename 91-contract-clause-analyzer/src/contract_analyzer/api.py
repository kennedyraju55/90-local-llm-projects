"""FastAPI REST API for Contract Clause Analyzer."""

from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

from .core import (
    analyze_clause,
    analyze_contract,
    compare_clauses,
    SAMPLE_CLAUSES,
    LEGAL_DISCLAIMER,
    check_ollama_running,
)

app = FastAPI(
    title="Contract Clause Analyzer API",
    description=(
        "AI-powered contract analysis with complete privacy. "
        "All processing happens locally via Ollama. "
        f"\n\n**Disclaimer:** {LEGAL_DISCLAIMER}"
    ),
    version="1.0.0",
)


class ClauseRequest(BaseModel):
    text: str = Field(..., description="Contract clause text to analyze")
    model: str = Field(default="gemma4:latest", description="Ollama model to use")


class ContractRequest(BaseModel):
    text: str = Field(..., description="Full contract text to analyze")
    model: str = Field(default="gemma4:latest", description="Ollama model to use")


class CompareRequest(BaseModel):
    clause_a: str = Field(..., description="First clause text")
    clause_b: str = Field(..., description="Second clause text")
    model: str = Field(default="gemma4:latest", description="Ollama model to use")


class ClauseResponse(BaseModel):
    clause_type: str
    risk_level: str
    summary: str
    obligations: List[str]
    deadlines: List[str]
    red_flags: List[str]
    recommendations: List[str]
    key_terms: List[str]


class ContractResponse(BaseModel):
    title: str
    overall_risk: str
    summary: str
    total_clauses: int
    high_risk_count: int
    obligations_count: int
    deadlines_count: int
    red_flags_count: int
    clauses: List[ClauseResponse]


class CompareResponse(BaseModel):
    differences: List[str]
    favorable_to_party_a: List[str]
    favorable_to_party_b: List[str]
    negotiation_points: List[str]
    recommendation: str


@app.get("/health")
async def health():
    """Health check endpoint."""
    ollama_ok = check_ollama_running()
    return {
        "status": "healthy" if ollama_ok else "degraded",
        "ollama": "connected" if ollama_ok else "disconnected",
        "service": "contract-clause-analyzer"
    }


@app.post("/analyze/clause", response_model=ClauseResponse)
async def api_analyze_clause(request: ClauseRequest):
    """Analyze a single contract clause."""
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Clause text is required")
    result = analyze_clause(request.text, model=request.model)
    return ClauseResponse(
        clause_type=result.clause_type,
        risk_level=result.risk_level,
        summary=result.summary,
        obligations=result.obligations,
        deadlines=result.deadlines,
        red_flags=result.red_flags,
        recommendations=result.recommendations,
        key_terms=result.key_terms
    )


@app.post("/analyze/contract", response_model=ContractResponse)
async def api_analyze_contract(request: ContractRequest):
    """Analyze a full contract document."""
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Contract text is required")
    result = analyze_contract(request.text, model=request.model)
    clauses = [
        ClauseResponse(
            clause_type=c.clause_type, risk_level=c.risk_level, summary=c.summary,
            obligations=c.obligations, deadlines=c.deadlines, red_flags=c.red_flags,
            recommendations=c.recommendations, key_terms=c.key_terms
        )
        for c in result.clause_analyses
    ]
    return ContractResponse(
        title=result.title, overall_risk=result.overall_risk, summary=result.summary,
        total_clauses=result.total_clauses, high_risk_count=result.high_risk_count,
        obligations_count=result.obligations_count, deadlines_count=result.deadlines_count,
        red_flags_count=result.red_flags_count, clauses=clauses
    )


@app.post("/compare", response_model=CompareResponse)
async def api_compare_clauses(request: CompareRequest):
    """Compare two contract clauses."""
    if not request.clause_a.strip() or not request.clause_b.strip():
        raise HTTPException(status_code=400, detail="Both clauses are required")
    result = compare_clauses(request.clause_a, request.clause_b, model=request.model)
    return CompareResponse(
        differences=result.get("differences", []),
        favorable_to_party_a=result.get("favorable_to_party_a", []),
        favorable_to_party_b=result.get("favorable_to_party_b", []),
        negotiation_points=result.get("negotiation_points", []),
        recommendation=result.get("recommendation", "")
    )


@app.get("/samples")
async def get_samples():
    """Get sample contract clauses for testing."""
    return {"samples": SAMPLE_CLAUSES}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
