# Multi-stage build for Legal Case Researcher
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

ENV PYTHONUNBUFFERED=1
ENV OLLAMA_HOST=http://ollama:11434

EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8501/_stcore/health')" || exit 1

CMD ["streamlit", "run", "src/case_researcher/web_ui.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]
