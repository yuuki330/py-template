.PHONY: help sync format lint test check clean

help:
	@echo "sync    - Install dependencies"
	@echo "format  - Format code with ruff"
	@echo "lint    - Lint code with ruff"
	@echo "test    - Run tests with pytest"
	@echo "check   - Run lint + test"
	@echo "clean   - Remove cache files"

sync:
	uv sync

format:
	uv run ruff format .

lint:
	uv run ruff check .

test:
	uv run pytest

check:
	uv run ruff check .
	uv run pytest

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +
