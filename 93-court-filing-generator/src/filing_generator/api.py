"""FastAPI REST API for Court Filing Generator.

Provides HTTP endpoints for generating court filings, motions,
and discovery requests using a local LLM.
"""

import sys
import os
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.filing_generator.core import (
    LEGAL_DISCLAIMER,
    CaseInfo,
    FilingType,
    FILING_TEMPLATES,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
)
from common.llm_client import check_ollama_running

# ─── App Setup ───────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Court Filing Generator API",
    description=(
        "AI-powered legal document generation API. "
        "100% local processing with Gemma 4 via Ollama. "
        "No data ever leaves your machine."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Pydantic Models ────────────────────────────────────────────────────────────

class CaseInfoRequest(BaseModel):
    """Case information for a filing request."""
    case_number: str = Field(..., description="Case number", examples=["2025-CV-01234"])
    court: str = Field(
        default="United States District Court",
        description="Court name",
    )
    parties: Dict[str, str] = Field(
        ...,
        description="Parties involved",
        examples=[{"plaintiff": "Jane Doe", "defendant": "Acme Corp"}],
    )
    judge: str = Field(default="", description="Presiding judge")
    jurisdiction: str = Field(default="federal", description="Jurisdiction type")


class FilingRequest(BaseModel):
    """Request to generate a court filing."""
    filing_type: str = Field(
        ...,
        description="Type of filing",
        examples=["motion_to_dismiss"],
    )
    case_info: CaseInfoRequest
    facts: str = Field(default="", description="Statement of facts")
    arguments: str = Field(default="", description="Legal arguments")
    model: str = Field(default="gemma4:latest", description="LLM model")


class MotionRequest(BaseModel):
    """Request to generate a legal motion."""
    motion_type: str = Field(
        ...,
        description="Type of motion",
        examples=["motion_to_dismiss"],
    )
    case_info: CaseInfoRequest
    grounds: str = Field(..., description="Grounds for the motion")
    model: str = Field(default="gemma4:latest", description="LLM model")


class DiscoveryRequest(BaseModel):
    """Request to generate discovery requests."""
    case_info: CaseInfoRequest
    discovery_type: str = Field(
        ...,
        description="Type of discovery",
        examples=["interrogatories"],
    )
    items: List[str] = Field(
        ...,
        description="Discovery topics/items",
        examples=[["employment records", "communications"]],
    )
    model: str = Field(default="gemma4:latest", description="LLM model")


class ValidationRequest(BaseModel):
    """Request to validate a filing."""
    filing_text: str = Field(..., description="Full text of the filing to validate")
    model: str = Field(default="gemma4:latest", description="LLM model")


class FilingResponse(BaseModel):
    """Response containing a generated filing."""
    filing_type: str
    title: str
    content: str
    sections: List[str]
    warnings: List[str]
    disclaimer: str = LEGAL_DISCLAIMER


class ValidationResponse(BaseModel):
    """Response containing validation results."""
    is_valid: bool
    score: int
    issues: List[str]
    missing_sections: List[str]
    suggestions: List[str]
    citation_check: str


# ─── Helper ──────────────────────────────────────────────────────────────────────

def _to_case_info(req: CaseInfoRequest) -> CaseInfo:
    """Convert a Pydantic CaseInfoRequest to a CaseInfo dataclass."""
    return CaseInfo(
        case_number=req.case_number,
        court=req.court,
        parties=req.parties,
        judge=req.judge,
        jurisdiction=req.jurisdiction,
    )


def _check_llm() -> None:
    """Raise HTTPException if Ollama is not running."""
    if not check_ollama_running():
        raise HTTPException(
            status_code=503,
            detail="Ollama is not running. Start it with: ollama serve",
        )


# ─── Endpoints ───────────────────────────────────────────────────────────────────

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Check API and Ollama health status."""
    ollama_ok = check_ollama_running()
    return {
        "status": "healthy" if ollama_ok else "degraded",
        "api": "running",
        "ollama": "connected" if ollama_ok else "disconnected",
        "privacy": "100% local processing",
        "version": "1.0.0",
    }


@app.post("/generate", response_model=FilingResponse)
async def generate_filing_endpoint(request: FilingRequest) -> FilingResponse:
    """Generate a court filing document."""
    _check_llm()

    try:
        case_info = _to_case_info(request.case_info)
        result = generate_filing(
            filing_type=request.filing_type,
            case_info=case_info,
            facts=request.facts,
            arguments=request.arguments,
            model=request.model,
        )
        return FilingResponse(
            filing_type=result.filing_type,
            title=result.title,
            content=result.content,
            sections=result.sections,
            warnings=result.warnings,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/motion", response_model=FilingResponse)
async def generate_motion_endpoint(request: MotionRequest) -> FilingResponse:
    """Generate a legal motion."""
    _check_llm()

    try:
        case_info = _to_case_info(request.case_info)
        result = generate_motion(
            motion_type=request.motion_type,
            case_info=case_info,
            grounds=request.grounds,
            model=request.model,
        )
        return FilingResponse(
            filing_type=result.filing_type,
            title=result.title,
            content=result.content,
            sections=result.sections,
            warnings=result.warnings,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/discovery", response_model=FilingResponse)
async def generate_discovery_endpoint(request: DiscoveryRequest) -> FilingResponse:
    """Generate discovery requests."""
    _check_llm()

    try:
        case_info = _to_case_info(request.case_info)
        result = generate_discovery_request(
            case_info=case_info,
            discovery_type=request.discovery_type,
            items=request.items,
            model=request.model,
        )
        return FilingResponse(
            filing_type=result.filing_type,
            title=result.title,
            content=result.content,
            sections=result.sections,
            warnings=result.warnings,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/validate", response_model=ValidationResponse)
async def validate_filing_endpoint(request: ValidationRequest) -> ValidationResponse:
    """Validate a court filing for completeness."""
    _check_llm()

    try:
        result = validate_filing(
            filing_text=request.filing_text,
            model=request.model,
        )
        return ValidationResponse(
            is_valid=result.get("is_valid", False),
            score=result.get("score", 0),
            issues=result.get("issues", []),
            missing_sections=result.get("missing_sections", []),
            suggestions=result.get("suggestions", []),
            citation_check=result.get("citation_check", "Not assessed"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/templates")
async def list_templates() -> Dict[str, Any]:
    """List all available filing templates."""
    templates = {}
    for ft, template in FILING_TEMPLATES.items():
        templates[ft.value] = {
            "title": template["title"],
            "sections": template["sections"],
            "description": template["description"],
        }
    return {
        "templates": templates,
        "total": len(templates),
    }
