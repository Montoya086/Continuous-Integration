.PHONY: help install install-dev test test-cov lint format clean pre-commit-install pre-commit-run

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

install-dev: ## Install the package in development mode with dev dependencies
	pip install -e ".[dev]"

test: ## Run tests
	python scripts/run_tests.py

test-cov: ## Run tests with coverage
	if [ -d "tests" ] && [ "$$(find tests -name 'test_*.py' -o -name '*_test.py' | wc -l)" -gt 0 ]; then \
		pytest --cov=src --cov-report=html --cov-report=term-missing; \
	else \
		echo "✅ No tests found - skipping test execution"; \
	fi

lint: ## Run linting
	flake8 src tests
	black --check src tests
	isort --check-only src tests

format: ## Format code
	black src tests
	isort src tests

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .coverage.xml

pre-commit-install: ## Install pre-commit hooks
	pre-commit install

pre-commit-run: ## Run pre-commit hooks on all files
	pre-commit run --all-files

ci: lint test ## Run CI pipeline locally
