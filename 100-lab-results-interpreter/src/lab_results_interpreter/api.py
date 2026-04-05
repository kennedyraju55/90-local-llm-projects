"""
Lab Results Interpreter - FastAPI REST API
RESTful API for programmatic lab result analysis.
"""

import os
import sys
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab_results_interpreter.core import (
    interpret_results,
    identify_abnormalities,
    suggest_followup_tests,
    explain_lab_value,
    get_reference_range,
    display_disclaimer,
    REFERENCE_RANGES,
    LAB_PANELS,
)
from common.llm_client import check_ollama_running

# ─── FastAPI App ─────────────────────────────────────────────────────

app = FastAPI(
    title="Lab Results Interpreter API",
    description=(
        "AI-powered laboratory result analysis API. "
        "100% local processing — no patient data leaves the machine."
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


# ─── Request / Response Models ───────────────────────────────────────


class InterpretRequest(BaseModel):
    lab_results: str = Field(..., description="Lab results text to interpret")
    patient_context: str = Field("", description="Patient context (age, sex, medications)")
    panel_type: str = Field("", description="Lab panel type (e.g., CBC, BMP)")


class AbnormalitiesRequest(BaseModel):
    lab_results: str = Field(..., description="Lab results text to analyze")
    panel_type: str = Field("", description="Lab panel type")


class FollowupRequest(BaseModel):
    lab_results: str = Field(..., description="Lab results text")
    clinical_context: str = Field("", description="Clinical context")


class ExplainRequest(BaseModel):
    test_name: str = Field(..., description="Lab test name")
    value: str = Field(..., description="Test result value")
    unit: str = Field("", description="Unit of measurement")


class InterpretResponse(BaseModel):
    interpretation: str
    panel_type: str
    disclaimer: str


class AbnormalitiesResponse(BaseModel):
    abnormalities: str
    panel_type: str
    disclaimer: str


class FollowupResponse(BaseModel):
    recommendations: str
    disclaimer: str


class ExplainResponse(BaseModel):
    explanation: str
    disclaimer: str


class HealthResponse(BaseModel):
    status: str
    ollama_running: bool
    version: str


# ─── Endpoints ───────────────────────────────────────────────────────


@app.get("/health", response_model=HealthResponse)
async def health():
    """Check API and Ollama health status."""
    return HealthResponse(
        status="healthy",
        ollama_running=check_ollama_running(),
        version="1.0.0",
    )


@app.post("/interpret", response_model=InterpretResponse)
async def api_interpret(request: InterpretRequest):
    """Interpret lab results using AI."""
    if not request.lab_results.strip():
        raise HTTPException(status_code=400, detail="Lab results text is required")

    result = interpret_results(
        lab_results_text=request.lab_results,
        patient_context=request.patient_context,
        panel_type=request.panel_type,
    )

    return InterpretResponse(
        interpretation=result,
        panel_type=request.panel_type or "auto-detected",
        disclaimer=display_disclaimer(),
    )


@app.post("/abnormalities", response_model=AbnormalitiesResponse)
async def api_abnormalities(request: AbnormalitiesRequest):
    """Identify abnormal values in lab results."""
    if not request.lab_results.strip():
        raise HTTPException(status_code=400, detail="Lab results text is required")

    result = identify_abnormalities(
        lab_results_text=request.lab_results,
        panel_type=request.panel_type,
    )

    return AbnormalitiesResponse(
        abnormalities=result,
        panel_type=request.panel_type or "auto-detected",
        disclaimer=display_disclaimer(),
    )


@app.post("/followup", response_model=FollowupResponse)
async def api_followup(request: FollowupRequest):
    """Suggest follow-up tests based on results."""
    if not request.lab_results.strip():
        raise HTTPException(status_code=400, detail="Lab results text is required")

    result = suggest_followup_tests(
        lab_results_text=request.lab_results,
        clinical_context=request.clinical_context,
    )

    return FollowupResponse(
        recommendations=result,
        disclaimer=display_disclaimer(),
    )


@app.post("/explain", response_model=ExplainResponse)
async def api_explain(request: ExplainRequest):
    """Explain a specific lab value."""
    if not request.test_name.strip():
        raise HTTPException(status_code=400, detail="Test name is required")

    result = explain_lab_value(
        test_name=request.test_name,
        value=request.value,
        unit=request.unit,
    )

    return ExplainResponse(
        explanation=result,
        disclaimer=display_disclaimer(),
    )


@app.get("/reference-ranges/{panel}")
async def api_reference_ranges(panel: str):
    """Get reference ranges for a specific lab panel."""
    if panel not in REFERENCE_RANGES:
        raise HTTPException(
            status_code=404,
            detail=f"Panel '{panel}' not found. Available: {list(REFERENCE_RANGES.keys())}",
        )

    return {
        "panel": panel,
        "ranges": REFERENCE_RANGES[panel],
    }


@app.get("/panels")
async def api_panels():
    """List all available lab panels."""
    return {
        "panels": LAB_PANELS,
        "panels_with_reference_data": list(REFERENCE_RANGES.keys()),
    }


@app.get("/disclaimer")
async def api_disclaimer():
    """Get the medical disclaimer."""
    return {"disclaimer": display_disclaimer()}
