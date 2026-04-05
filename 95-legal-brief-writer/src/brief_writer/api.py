"""FastAPI REST API for Legal Brief Writer."""

import os
import sys
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.brief_writer.core import (
    BriefType,
    CaseDetails,
    LEGAL_DISCLAIMER,
    BRIEF_TEMPLATES,
    write_brief,
    write_memorandum,
    write_irac_analysis,
    generate_table_of_authorities,
    improve_legal_writing,
    format_brief_text,
    format_irac_text,
)
from src.brief_writer.config import load_config
from common.llm_client import check_ollama_running

# ---------------------------------------------------------------------------
# Pydantic Models
# ---------------------------------------------------------------------------


class CaseDetailsModel(BaseModel):
    """Case details input model."""
    case_name: str = Field(..., description="Name of the case")
    case_number: str = Field("", description="Case number")
    court: str = Field("", description="Court name")
    jurisdiction: str = Field("", description="Jurisdiction")
    client_position: str = Field("", description="Client's position")
    opposing_party: str = Field("", description="Opposing party name")


class BriefRequest(BaseModel):
    """Request model for brief generation."""
    brief_type: str = Field("memorandum_of_law", description="Type of brief")
    case_details: CaseDetailsModel
    facts: str = Field(..., description="Statement of facts")
    issues: str = Field(..., description="Legal issues to address")
    arguments: str = Field("", description="Key arguments")
    model: Optional[str] = Field(None, description="LLM model override")


class MemorandumRequest(BaseModel):
    """Request model for memorandum generation."""
    case_details: CaseDetailsModel
    question_presented: str = Field(..., description="Question presented")
    facts: str = Field(..., description="Statement of facts")
    model: Optional[str] = Field(None, description="LLM model override")


class IRACRequest(BaseModel):
    """Request model for IRAC analysis."""
    issue: str = Field(..., description="Legal issue to analyze")
    facts: str = Field(..., description="Relevant facts")
    model: Optional[str] = Field(None, description="LLM model override")


class ImproveRequest(BaseModel):
    """Request model for writing improvement."""
    text: str = Field(..., description="Legal text to improve")
    model: Optional[str] = Field(None, description="LLM model override")


class TOARequest(BaseModel):
    """Request model for Table of Authorities generation."""
    brief_text: str = Field(..., description="Full text of the brief")
    model: Optional[str] = Field(None, description="LLM model override")


class BriefSectionResponse(BaseModel):
    """Brief section in response."""
    title: str
    content: str
    order: int


class LegalIssueResponse(BaseModel):
    """Legal issue in response."""
    issue: str
    rule: str
    analysis: str
    conclusion: str


class BriefResponse(BaseModel):
    """Response model for brief generation."""
    brief_type: str
    title: str
    sections: List[BriefSectionResponse]
    legal_issues: List[LegalIssueResponse]
    word_count: int
    warnings: List[str]
    table_of_authorities: List[str]
    formatted_text: str


class IRACResponse(BaseModel):
    """Response model for IRAC analysis."""
    issue: str
    rule: str
    analysis: str
    conclusion: str
    formatted_text: str


class ImproveResponse(BaseModel):
    """Response model for writing improvement."""
    improved_text: str
    changes: List[str]
    suggestions: List[str]
    readability_score: str
    legal_accuracy_notes: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    ollama_running: bool
    model: str
    version: str


class TemplateResponse(BaseModel):
    """Brief template info."""
    brief_type: str
    description: str
    sections: List[str]


# ---------------------------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Legal Brief Writer API",
    description="AI-powered legal brief and memoranda generation. 100% local processing.",
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


def _get_model(override: Optional[str] = None) -> str:
    """Get model name with optional override."""
    if override:
        return override
    config = load_config()
    return os.environ.get("LLM_MODEL", config.llm.model)


def _to_case_details(cd: CaseDetailsModel) -> CaseDetails:
    """Convert Pydantic model to dataclass."""
    return CaseDetails(
        case_name=cd.case_name,
        case_number=cd.case_number,
        court=cd.court,
        jurisdiction=cd.jurisdiction,
        client_position=cd.client_position,
        opposing_party=cd.opposing_party,
    )


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check API and Ollama health status."""
    config = load_config()
    return HealthResponse(
        status="healthy",
        ollama_running=check_ollama_running(),
        model=config.llm.model,
        version="1.0.0",
    )


@app.post("/brief", response_model=BriefResponse)
async def create_brief(request: BriefRequest):
    """Generate a legal brief."""
    try:
        model = _get_model(request.model)
        case_details = _to_case_details(request.case_details)

        result = write_brief(
            brief_type=request.brief_type,
            case_details=case_details,
            facts=request.facts,
            issues=request.issues,
            arguments=request.arguments,
            model=model,
        )

        return BriefResponse(
            brief_type=result.brief_type,
            title=result.title,
            sections=[
                BriefSectionResponse(title=s.title, content=s.content, order=s.order)
                for s in result.sections
            ],
            legal_issues=[
                LegalIssueResponse(
                    issue=li.issue, rule=li.rule,
                    analysis=li.analysis, conclusion=li.conclusion,
                )
                for li in result.legal_issues
            ],
            word_count=result.word_count,
            warnings=result.warnings,
            table_of_authorities=result.table_of_authorities,
            formatted_text=format_brief_text(result),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/memorandum", response_model=BriefResponse)
async def create_memorandum(request: MemorandumRequest):
    """Generate a legal memorandum."""
    try:
        model = _get_model(request.model)
        case_details = _to_case_details(request.case_details)

        result = write_memorandum(
            case_details=case_details,
            question_presented=request.question_presented,
            facts=request.facts,
            model=model,
        )

        return BriefResponse(
            brief_type=result.brief_type,
            title=result.title,
            sections=[
                BriefSectionResponse(title=s.title, content=s.content, order=s.order)
                for s in result.sections
            ],
            legal_issues=[
                LegalIssueResponse(
                    issue=li.issue, rule=li.rule,
                    analysis=li.analysis, conclusion=li.conclusion,
                )
                for li in result.legal_issues
            ],
            word_count=result.word_count,
            warnings=result.warnings,
            table_of_authorities=result.table_of_authorities,
            formatted_text=format_brief_text(result),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/irac", response_model=IRACResponse)
async def create_irac(request: IRACRequest):
    """Perform IRAC analysis."""
    try:
        model = _get_model(request.model)

        result = write_irac_analysis(
            issue=request.issue,
            facts=request.facts,
            model=model,
        )

        return IRACResponse(
            issue=result.issue,
            rule=result.rule,
            analysis=result.analysis,
            conclusion=result.conclusion,
            formatted_text=format_irac_text(result),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/improve", response_model=ImproveResponse)
async def improve_writing(request: ImproveRequest):
    """Improve legal writing."""
    try:
        model = _get_model(request.model)
        result = improve_legal_writing(text=request.text, model=model)

        return ImproveResponse(
            improved_text=result["improved_text"],
            changes=result.get("changes", []),
            suggestions=result.get("suggestions", []),
            readability_score=result.get("readability_score", "N/A"),
            legal_accuracy_notes=result.get("legal_accuracy_notes", ""),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/templates", response_model=List[TemplateResponse])
async def list_templates():
    """List available brief templates."""
    templates = []
    for bt in BriefType:
        template = BRIEF_TEMPLATES.get(bt, {})
        templates.append(TemplateResponse(
            brief_type=bt.value,
            description=template.get("description", ""),
            sections=template.get("sections", []),
        ))
    return templates


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
