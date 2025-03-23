run:
	PYTHONPATH=src uv run python -m src.ammoseekr.main

dryrun:
	PYTHONPATH=src uv run python -m src.ammoseekr.main --dry-run --verbose

test:
	PYTHONPATH=src uv run pytest

format:
	uv run ruff format src tests infra

lint:
	uv run ruff check src tests infra

fix:
	uv run ruff check --fix src tests infra

set-env:
	export `xargs < .env`