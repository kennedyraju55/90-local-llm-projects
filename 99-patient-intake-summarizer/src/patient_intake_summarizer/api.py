"""Patient Intake Summarizer API - AI-powered intake form summarization.

⚠️ DISCLAIMER: AI-generated summaries are for clinical decision support only.
All output must be reviewed by a licensed physician. This tool runs 100% locally
— no patient data leaves this machine (HIPAA-friendly).
"""

from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .core import (
    DISCLAIMER,
    INTAKE_CATEGORIES,
    summarize_intake,
    extract_medical_history,
    generate_pre_visit_summary,
    identify_risk_factors,
    flag_missing_info,
)

CLINICAL_DISCLAIMER = (
    "⚠️ AI-generated summaries are for clinical decision support only. "
    "All output must be reviewed by a licensed physician. "
    "No patient data leaves this machine (HIPAA-friendly)."
)

app = FastAPI(
    title="Patient Intake Summarizer",
    description=(
        "AI-powered patient intake form summarization, medical history extraction, "
        "risk factor identification, and pre-visit summary generation.\n\n"
        f"**{CLINICAL_DISCLAIMER}**"
    ),
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Request / Response Models
# ---------------------------------------------------------------------------

class SummarizeRequest(BaseModel):
    intake_text: str = Field(..., description="Raw patient intake form text.")
    summary_format: str = Field(
        "structured",
        description="Summary format: 'brief', 'detailed', or 'structured'.",
    )
    focus_areas: Optional[List[str]] = Field(
        None,
        description="Optional list of intake categories to focus on.",
    )


class SummarizeResponse(BaseModel):
    summary: str


class ExtractHistoryRequest(BaseModel):
    intake_text: str = Field(..., description="Raw patient intake form text.")


class ExtractHistoryResponse(BaseModel):
    history: dict


class PreVisitRequest(BaseModel):
    intake_data: dict = Field(..., description="Categorized intake data dictionary.")
    appointment_type: str = Field(
        "general",
        description="Appointment type: general, follow-up, specialist, annual_physical, urgent.",
    )


class PreVisitResponse(BaseModel):
    summary: str


class RiskFactorsRequest(BaseModel):
    intake_text: str = Field(..., description="Raw patient intake form text.")


class RiskFactorsResponse(BaseModel):
    risk_factors: List[str]


class MissingInfoRequest(BaseModel):
    intake_text: str = Field(..., description="Raw patient intake form text.")


class MissingInfoResponse(BaseModel):
    missing_items: List[str]


class CategoriesResponse(BaseModel):
    categories: dict


class DisclaimerResponse(BaseModel):
    disclaimer: str


class HealthResponse(BaseModel):
    status: str
    service: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Check API health status."""
    return HealthResponse(status="healthy", service="patient-intake-summarizer")


@app.post("/summarize", response_model=SummarizeResponse, tags=["Summarization"])
async def summarize(request: SummarizeRequest):
    """Summarize patient intake form text into a clinical summary."""
    try:
        result = summarize_intake(
            intake_text=request.intake_text,
            summary_format=request.summary_format,
            focus_areas=request.focus_areas,
        )
        return SummarizeResponse(summary=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {e}")


@app.post("/extract-history", response_model=ExtractHistoryResponse, tags=["Extraction"])
async def extract_history(request: ExtractHistoryRequest):
    """Extract and categorize medical history from intake text."""
    try:
        result = extract_medical_history(request.intake_text)
        return ExtractHistoryResponse(history=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"History extraction failed: {e}")


@app.post("/pre-visit-summary", response_model=PreVisitResponse, tags=["Summarization"])
async def pre_visit_summary(request: PreVisitRequest):
    """Generate a pre-visit summary for the physician."""
    try:
        result = generate_pre_visit_summary(
            intake_data=request.intake_data,
            appointment_type=request.appointment_type,
        )
        return PreVisitResponse(summary=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pre-visit summary failed: {e}")


@app.post("/risk-factors", response_model=RiskFactorsResponse, tags=["Analysis"])
async def risk_factors(request: RiskFactorsRequest):
    """Identify clinical risk factors from intake text."""
    try:
        result = identify_risk_factors(request.intake_text)
        return RiskFactorsResponse(risk_factors=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Risk factor analysis failed: {e}")


@app.post("/missing-info", response_model=MissingInfoResponse, tags=["Analysis"])
async def missing_info(request: MissingInfoRequest):
    """Flag missing or incomplete information in the intake form."""
    try:
        result = flag_missing_info(request.intake_text)
        return MissingInfoResponse(missing_items=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Missing info check failed: {e}")


@app.get("/categories", response_model=CategoriesResponse, tags=["Info"])
async def get_categories():
    """Return the standard intake form categories."""
    return CategoriesResponse(categories=INTAKE_CATEGORIES)


@app.get("/disclaimer", response_model=DisclaimerResponse, tags=["Info"])
async def get_disclaimer():
    """Return the clinical disclaimer for this service."""
    return DisclaimerResponse(disclaimer=DISCLAIMER)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
