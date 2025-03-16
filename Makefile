run:
	PYTHONPATH=src python -m src.ammoseekr.main

test:
	PYTHONPATH=src pytest

format:
	uv run ruff format src tests
