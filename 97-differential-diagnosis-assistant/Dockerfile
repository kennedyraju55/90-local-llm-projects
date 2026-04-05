# ============================================================
# Dockerfile for Differential Diagnosis Assistant
# ============================================================
# MEDICAL DISCLAIMER: This application is for informational
# and educational purposes only. It is NOT a substitute for
# professional medical advice, diagnosis, or treatment. Always
# seek the advice of a qualified healthcare provider with any
# questions regarding a medical condition.
# ============================================================

# --------------- Stage 1: Builder ---------------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements*.txt setup.py ./

RUN pip install --no-cache-dir -e .

# --------------- Stage 2: Runtime ---------------
FROM python:3.11-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source
COPY . .

# Environment configuration
ENV OLLAMA_HOST=http://host.docker.internal:11434
ENV PYTHONUNBUFFERED=1

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "src/differential_diagnosis/web_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
