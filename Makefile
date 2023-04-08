# Makefile for Django project

# Variables
POETRY = poetry
MANAGE = $(POETRY) run python homedb/manage.py
DJANGO_SETTINGS_MODULE ?= homedb.settings
export DJANGO_SETTINGS_MODULE

# Targets

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  help         - Display this help message"
	@echo "  install      - Install project requirements"
	@echo "  migrate      - Run database migrations"
	@echo "  makemigrations - Create new migrations"
	@echo "  runserver    - Run the development server"
	@echo "  test         - Run the test suite"
	@echo "  lint         - Run linters"
	@echo "  superuser    - Create a Django superuser"

.PHONY: install
install:
	$(POETRY) install

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

.PHONY: runserver
runserver:
	$(MANAGE) runserver

.PHONY: test
test:
	$(MANAGE) test

.PHONY: lint
lint:
	$(POETRY) run ruff .

.PHONY: superuser
superuser:
	$(MANAGE) createsuperuser

.PHONY: format
format:
	$(POETRY) run isort .
	$(POETRY) run black .
