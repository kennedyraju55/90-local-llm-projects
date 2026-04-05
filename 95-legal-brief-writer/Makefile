.PHONY: all install test lint format run-web run-api run-cli clean docker-build docker-up docker-down help

PYTHON ?= python
PIP ?= pip
PROJECT_DIR = src/brief_writer

all: install test lint ## Install, test, and lint

install: ## Install dependencies
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

test: ## Run tests
	$(PYTHON) -m pytest tests/ -v --tb=short

test-cov: ## Run tests with coverage
	$(PYTHON) -m pytest tests/ -v --cov=$(PROJECT_DIR) --cov-report=term-missing --cov-report=html

lint: ## Run linting
	$(PYTHON) -m py_compile $(PROJECT_DIR)/core.py
	$(PYTHON) -m py_compile $(PROJECT_DIR)/cli.py
	$(PYTHON) -m py_compile $(PROJECT_DIR)/api.py
	$(PYTHON) -m py_compile $(PROJECT_DIR)/web_ui.py
	$(PYTHON) -m py_compile $(PROJECT_DIR)/config.py
	@echo "✅ All files compile successfully"

format: ## Format code with black
	black $(PROJECT_DIR)/ tests/ examples/

run-web: ## Run Streamlit web UI
	streamlit run $(PROJECT_DIR)/web_ui.py --server.port 8501

run-api: ## Run FastAPI server
	uvicorn $(PROJECT_DIR).api:app --host 0.0.0.0 --port 8000 --reload

run-cli: ## Show CLI help
	$(PYTHON) -m $(PROJECT_DIR).cli --help

demo: ## Run demo script
	$(PYTHON) examples/demo.py

docker-build: ## Build Docker image
	docker build -t legal-brief-writer .

docker-up: ## Start Docker services
	docker-compose up -d

docker-down: ## Stop Docker services
	docker-compose down

clean: ## Clean build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name *.egg-info -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

help: ## Show this help message
	@echo "Legal Brief Writer - Available targets:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
