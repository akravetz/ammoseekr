run:
	PYTHONPATH=src uv run python -m src.ammoseekr.main

test:
	PYTHONPATH=src uv run pytest

format:
	uv run ruff format src tests
