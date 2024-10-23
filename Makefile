help:
	@echo ""
	@echo "Options:"
	@echo ""
	@echo "- make help          Show this help"
	@echo ""
	@echo "CODE CHECKS AND FORMATTING"
	@echo "- make check         Run code quality checker"
	@echo "- make fix           Let code quality checker auto-fix problems"
	@echo "- make format        Run the code formatter"
	@echo "- make mypy          Run mypy (checks typing)"
	@echo ""
	@echo "UNIT TESTING"
	@echo "- make test          Run unit tests"
	@echo ""
	@echo "INTEGRATION TESTING"
	@echo "- make istart        Start support containers for integration testing"
	@echo "- make itest         Run integration tests (against integration containers)"
	@echo "- make alltests      Run all tests (unit + integration)"
	@echo "- make run           Start the application"
	@echo "- make istop         Tear down support containers"
	@echo ""
	@echo "DOCKER TESTING"
	@echo "- make docker-build  Build docker images locally"
	@echo "- make docker-run    Run core app in docker, using the integration containers"
	@echo "- make docker-test   Run all tests (unit + integration) in Docker"
	@echo ""
	@echo "VARIA"
	@echo "- make priv          Run environment that integrates with DUSTool priv env"
	@echo "- make migrations    Generate migration files when the ORM models have changed"
	@echo ""


test:
	@coverage run -m pytest tests/unit/
	@coverage xml
	@coverage report --show-missing --skip-covered

itest:
	@coverage run -m pytest tests/integration/
	@coverage xml
	@coverage report --show-missing --skip-covered

alltests:
	@coverage run -m pytest -s tests/unit tests/integration
	@coverage xml
	@coverage report --show-missing --skip-covered

checks: format sort

format:
	@ruff format

sort:
	@ruff check --select I --fix .

mypy:
	mypy src/ tests/

run:
	@export APP_ENVIRONMENT=production && bin/testctl run

config:
	@export APP_ENVIRONMENT=development && bin/testctl config


migrations:
	@export APP_ENVIRONMENT=production && bin/generate_migrations