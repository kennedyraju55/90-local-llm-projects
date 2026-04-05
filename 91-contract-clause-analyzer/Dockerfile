# ============================================================
# Dockerfile for Contract Clause Analyzer
# ============================================================
# LEGAL DISCLAIMER: This application provides AI-assisted
# contract analysis for informational purposes only. It is
# NOT legal advice.
# ============================================================

# --------------- Stage 1: Builder ---------------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt setup.py ./
COPY src/ src/

RUN pip install --no-cache-dir -r requirements.txt

# --------------- Stage 2: Runtime ---------------
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

ENV OLLAMA_HOST=http://host.docker.internal:11434
ENV PYTHONUNBUFFERED=1

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "src/contract_analyzer/web_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
