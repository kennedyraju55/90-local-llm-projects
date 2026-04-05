"""Clinical Note Generator API - AI-powered SOAP note generation.

⚠️ MEDICAL DISCLAIMER: This API generates AI-assisted clinical note drafts for
informational purposes only. All output MUST be reviewed by a qualified physician.
"""

from typing import List, Optional, Dict, Any
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .core import (
    DISCLAIMER,
    NOTE_TEMPLATES,
    SPECIALTY_PROMPTS,
    generate_soap_note,
    generate_note_section,
    refine_note,
    extract_diagnoses,
)

MEDICAL_DISCLAIMER = (
    "⚠️ This API generates AI-assisted drafts for informational purposes only. "
    "All output MUST be reviewed and approved by a qualified physician before clinical use."
)

app = FastAPI(
    title="Clinical Note Generator API",
    description=f"AI-powered SOAP note generation from patient encounters.\n\n**{MEDICAL_DISCLAIMER}**",
    version="1.0.0",
)


class NoteRequest(BaseModel):
    encounter_description: str = Field(..., description="Free-text description of the patient encounter")
    patient_demographics: Optional[Dict[str, Any]] = Field(None, description="Patient demographics (age, sex, etc.)")
    note_type: str = Field("general", description="Type of clinical note")
    specialty: str = Field("internal_medicine", description="Medical specialty")


class NoteResponse(BaseModel):
    note: str
    disclaimer: str = MEDICAL_DISCLAIMER


class SectionRequest(BaseModel):
    encounter_description: str = Field(..., description="Encounter description")
    section: str = Field(..., description="SOAP section: S, O, A, or P")


class SectionResponse(BaseModel):
    section: str
    content: str
    disclaimer: str = MEDICAL_DISCLAIMER


class RefineRequest(BaseModel):
    original_note: str = Field(..., description="Original SOAP note")
    feedback: str = Field(..., description="Physician feedback for refinement")


class RefineResponse(BaseModel):
    refined_note: str
    disclaimer: str = MEDICAL_DISCLAIMER


class DiagnosesResponse(BaseModel):
    diagnoses: List[str]
    disclaimer: str = MEDICAL_DISCLAIMER


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Check API health status."""
    return HealthResponse(status="healthy", service="clinical-note-generator")


@app.post("/generate", response_model=NoteResponse, tags=["Notes"])
async def generate_note(request: NoteRequest):
    """Generate a complete SOAP note from an encounter description."""
    try:
        note = generate_soap_note(
            encounter_description=request.encounter_description,
            patient_demographics=request.patient_demographics,
            note_type=request.note_type,
            specialty=request.specialty,
        )
        return NoteResponse(note=note)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Note generation failed: {e}")


@app.post("/generate/section", response_model=SectionResponse, tags=["Notes"])
async def generate_section(request: SectionRequest):
    """Generate a specific SOAP section."""
    if request.section.upper() not in ["S", "O", "A", "P"]:
        raise HTTPException(status_code=400, detail="Section must be S, O, A, or P")
    try:
        content = generate_note_section(request.encounter_description, request.section)
        return SectionResponse(section=request.section.upper(), content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Section generation failed: {e}")


@app.post("/refine", response_model=RefineResponse, tags=["Notes"])
async def refine(request: RefineRequest):
    """Refine a SOAP note based on physician feedback."""
    try:
        refined = refine_note(request.original_note, request.feedback)
        return RefineResponse(refined_note=refined)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Refinement failed: {e}")


@app.post("/extract-diagnoses", response_model=DiagnosesResponse, tags=["Analysis"])
async def extract(request: NoteRequest):
    """Extract diagnoses from a generated note."""
    try:
        note = generate_soap_note(request.encounter_description)
        diagnoses = extract_diagnoses(note)
        return DiagnosesResponse(diagnoses=diagnoses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {e}")


@app.get("/templates", tags=["Info"])
async def get_templates():
    """List available note templates."""
    return {"templates": NOTE_TEMPLATES, "disclaimer": MEDICAL_DISCLAIMER}


@app.get("/specialties", tags=["Info"])
async def get_specialties():
    """List available specialties."""
    return {"specialties": list(SPECIALTY_PROMPTS.keys()), "disclaimer": MEDICAL_DISCLAIMER}


@app.get("/disclaimer", tags=["Info"])
async def get_disclaimer():
    """Return the medical disclaimer."""
    return {"disclaimer": DISCLAIMER}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
