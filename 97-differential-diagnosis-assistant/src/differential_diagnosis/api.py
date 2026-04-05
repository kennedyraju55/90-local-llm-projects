"""Differential Diagnosis Assistant API - AI-powered diagnostic reasoning.

⚠️ MEDICAL DISCLAIMER: This tool is for informational purposes only and does not
constitute medical advice, diagnosis, or treatment. Always seek the advice of a
qualified healthcare provider with any questions regarding a medical condition.
"""

from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .core import (
    DISCLAIMER,
    assess_urgency,
    get_affected_systems,
    generate_differential,
    get_workup_recommendations,
    compare_diagnoses,
)

MEDICAL_DISCLAIMER = (
    "⚠️ This API is for informational and educational purposes only and does not "
    "constitute medical advice, diagnosis, or treatment. Always consult a qualified "
    "healthcare provider for medical concerns. Differential diagnoses are AI-generated "
    "hypotheses and must NOT be used for clinical decision-making."
)

app = FastAPI(
    title="Differential Diagnosis Assistant",
    description=(
        "AI-powered diagnostic reasoning with ranked differentials and workup recommendations.\n\n"
        f"**{MEDICAL_DISCLAIMER}**"
    ),
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Request / Response Models
# ---------------------------------------------------------------------------

class DiagnoseRequest(BaseModel):
    symptoms: str = Field(..., description="Description of presenting symptoms.")
    patient_info: Optional[str] = Field("", description="Patient demographics, PMH, medications.")
    exam_findings: Optional[str] = Field("", description="Physical examination findings.")
    conversation_history: Optional[List[dict]] = Field(
        None,
        description="Optional prior conversation history for context.",
    )


class DiagnoseResponse(BaseModel):
    differential: str
    disclaimer: str = MEDICAL_DISCLAIMER


class WorkupRequest(BaseModel):
    diagnosis: str = Field(..., description="Diagnosis to get workup recommendations for.")


class WorkupResponse(BaseModel):
    recommendations: str
    disclaimer: str = MEDICAL_DISCLAIMER


class CompareRequest(BaseModel):
    diagnosis1: str = Field(..., description="First diagnosis to compare.")
    diagnosis2: str = Field(..., description="Second diagnosis to compare.")
    clinical_data: Optional[str] = Field("", description="Clinical context for comparison.")


class CompareResponse(BaseModel):
    comparison: str
    disclaimer: str = MEDICAL_DISCLAIMER


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
    return HealthResponse(status="healthy", service="differential-diagnosis-assistant")


@app.post("/diagnose", response_model=DiagnoseResponse, tags=["Diagnosis"])
async def diagnose(request: DiagnoseRequest):
    """Generate a ranked differential diagnosis from symptoms, patient info, and exam findings."""
    try:
        result = generate_differential(
            symptoms=request.symptoms,
            patient_info=request.patient_info or "",
            exam_findings=request.exam_findings or "",
            conversation_history=request.conversation_history,
        )
        return DiagnoseResponse(differential=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Differential diagnosis generation failed: {e}")


@app.post("/workup", response_model=WorkupResponse, tags=["Workup"])
async def workup(request: WorkupRequest):
    """Get recommended diagnostic workup for a specific diagnosis."""
    try:
        result = get_workup_recommendations(diagnosis=request.diagnosis)
        return WorkupResponse(recommendations=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workup recommendation failed: {e}")


@app.post("/compare", response_model=CompareResponse, tags=["Comparison"])
async def compare(request: CompareRequest):
    """Compare and contrast two diagnoses."""
    try:
        result = compare_diagnoses(
            diagnosis1=request.diagnosis1,
            diagnosis2=request.diagnosis2,
            clinical_data=request.clinical_data or "",
        )
        return CompareResponse(comparison=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Diagnosis comparison failed: {e}")


@app.get("/disclaimer", response_model=DisclaimerResponse, tags=["Info"])
async def get_disclaimer():
    """Return the medical disclaimer for this service."""
    return DisclaimerResponse(disclaimer=DISCLAIMER)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
