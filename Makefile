test:
	@coverage run -m pytest tests/unit/
	@coverage xml
	@coverage report --show-missing --skip-covered

itest:
	coverage run -m pytest tests/integration/
	coverage xml
	coverage report --show-missing --skip-covered

alltests:
	coverage run -m pytest -s tests/unit tests/integration
	coverage xml
	coverage report --show-missing --skip-covered

checks: format sort

format:
	@ruff format

sort:
	@ruff check --select I --fix .

mypy:
	mypy src/ tests/

run2:
	@export APP_ENVIRONMENT=development && bin/testctl run

config:
	@export APP_ENVIRONMENT=development && bin/testctl config

run:
	@bin/run run

migrations:
	@bin/generate_migrations