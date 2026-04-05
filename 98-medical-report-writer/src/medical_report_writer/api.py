"""Medical Report Writer API - AI-powered clinical report generation.

⚠️ DISCLAIMER: All generated reports MUST be reviewed and approved by a
licensed physician before clinical use. This tool is a drafting assistant
and does NOT constitute medical documentation without physician review.
"""

from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .core import (
    DISCLAIMER,
    REPORT_TYPES,
    generate_report,
    generate_discharge_summary,
    generate_referral_letter,
    format_report,
)

MEDICAL_DISCLAIMER = (
    "⚠️ This report is AI-drafted and MUST be reviewed, verified, and approved "
    "by a licensed physician before clinical use. All data is processed locally."
)

app = FastAPI(
    title="Medical Report Writer API",
    description=(
        "AI-powered clinical report generation using local LLMs.\n\n"
        f"**{MEDICAL_DISCLAIMER}**"
    ),
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Request / Response Models
# ---------------------------------------------------------------------------

class GenerateReportRequest(BaseModel):
    clinical_data: str = Field(..., description="Clinical data for the report.")
    report_type: str = Field(
        "progress_note",
        description="Type of report to generate.",
    )
    patient_demographics: Optional[str] = Field(
        None, description="Optional patient demographic information.",
    )
    conversation_history: Optional[List[dict]] = Field(
        None, description="Optional prior conversation history.",
    )


class GenerateReportResponse(BaseModel):
    report: str
    report_type: str
    disclaimer: str = MEDICAL_DISCLAIMER


class DischargeSummaryRequest(BaseModel):
    admission_data: str = Field(..., description="Admission details.")
    hospital_course: str = Field(..., description="Hospital course description.")
    discharge_info: str = Field(..., description="Discharge information.")


class DischargeSummaryResponse(BaseModel):
    summary: str
    disclaimer: str = MEDICAL_DISCLAIMER


class ReferralLetterRequest(BaseModel):
    patient_info: str = Field(..., description="Patient information.")
    reason: str = Field(..., description="Reason for referral.")
    clinical_findings: str = Field(..., description="Clinical findings.")
    requesting_physician: Optional[str] = Field(
        None, description="Referring physician name.",
    )


class ReferralLetterResponse(BaseModel):
    letter: str
    disclaimer: str = MEDICAL_DISCLAIMER


class FormatReportRequest(BaseModel):
    raw_report: str = Field(..., description="Raw report text to format.")
    style: str = Field("standard", description="Formatting style: standard, compact, detailed.")


class FormatReportResponse(BaseModel):
    formatted_report: str
    style: str


class ReportTypeInfo(BaseModel):
    key: str
    name: str
    description: str
    sections: str


class ReportTypesResponse(BaseModel):
    report_types: List[ReportTypeInfo]


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
    return HealthResponse(status="healthy", service="medical-report-writer")


@app.post("/generate", response_model=GenerateReportResponse, tags=["Reports"])
async def generate(request: GenerateReportRequest):
    """Generate a medical report from clinical data."""
    try:
        report = generate_report(
            clinical_data=request.clinical_data,
            report_type=request.report_type,
            patient_demographics=request.patient_demographics,
            conversation_history=request.conversation_history,
        )
        return GenerateReportResponse(report=report, report_type=request.report_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {e}")


@app.post("/discharge-summary", response_model=DischargeSummaryResponse, tags=["Reports"])
async def discharge_summary(request: DischargeSummaryRequest):
    """Generate a discharge summary."""
    try:
        summary = generate_discharge_summary(
            admission_data=request.admission_data,
            hospital_course=request.hospital_course,
            discharge_info=request.discharge_info,
        )
        return DischargeSummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Discharge summary generation failed: {e}")


@app.post("/referral-letter", response_model=ReferralLetterResponse, tags=["Reports"])
async def referral_letter(request: ReferralLetterRequest):
    """Generate a referral letter."""
    try:
        letter = generate_referral_letter(
            patient_info=request.patient_info,
            reason=request.reason,
            clinical_findings=request.clinical_findings,
            requesting_physician=request.requesting_physician,
        )
        return ReferralLetterResponse(letter=letter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Referral letter generation failed: {e}")


@app.post("/format", response_model=FormatReportResponse, tags=["Reports"])
async def format_existing_report(request: FormatReportRequest):
    """Format a raw report according to the specified style."""
    try:
        formatted = format_report(request.raw_report, request.style)
        return FormatReportResponse(formatted_report=formatted, style=request.style)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Formatting failed: {e}")


@app.get("/report-types", response_model=ReportTypesResponse, tags=["Info"])
async def get_report_types():
    """List all available report types."""
    types = [
        ReportTypeInfo(key=k, name=v["name"], description=v["description"], sections=v["sections"])
        for k, v in REPORT_TYPES.items()
    ]
    return ReportTypesResponse(report_types=types)


@app.get("/disclaimer", response_model=DisclaimerResponse, tags=["Info"])
async def get_disclaimer():
    """Return the medical disclaimer for this service."""
    return DisclaimerResponse(disclaimer=DISCLAIMER)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
