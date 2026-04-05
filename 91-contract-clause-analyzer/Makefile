.PHONY: install test lint run-cli run-web run-api clean docker-build docker-up docker-down

install:
	pip install -e ".[dev]"

test:
	python -m pytest tests/ -v --tb=short

lint:
	python -m py_compile src/contract_analyzer/core.py
	python -m py_compile src/contract_analyzer/cli.py
	python -m py_compile src/contract_analyzer/api.py
	python -m py_compile src/contract_analyzer/web_ui.py

run-cli:
	python -m contract_analyzer.cli

run-web:
	streamlit run src/contract_analyzer/web_ui.py

run-api:
	uvicorn src.contract_analyzer.api:app --host 0.0.0.0 --port 8000 --reload

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name *.egg-info -exec rm -rf {} +

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down
