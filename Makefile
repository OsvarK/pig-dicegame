VENV = .venv/Scripts/

PYTHON:
	$(venv)python

PIP:
	PYTHON $(venv)pip

# Install ----------------------------------------------------
setup:
	@echo Creating a virtual environment...
	python3 -m venv .venv
	@echo virtual environment was created!
	@echo Uppgrading pip...
	PIP install --upgrade pip
	@echo Setup is complete!
	@echo Now activate the virtual environment: '.venv/Scripts/activate'
	@echo after activation type 'make install'

install:
	@echo Installing requirements.txt...
	PIP install -r requirements.txt
	@echo installing the project... (this step is nessesary to run tests)
	PIP install .
	@echo All done, type pig for execution of application or run make commands for testing.

# Testing ----------------------------------------------------
unittest:
	- PYTHON -m unittest discover tests

coverage:
	- coverage run -m unittest discover tests
	- coverage html
	- coverage report -m

pylint:
	- pylint pigdicegame

flake8:
	- flake8 pigdicegame

test:
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running unittest----------------------------
	@echo --------------------------------------------------------------------------
	- PYTHON -m unittest discover tests
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running coverage ---------------------------
	@echo --------------------------------------------------------------------------
	- coverage run -m unittest discover tests
	- coverage html
	- coverage report -m
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running pylint -----------------------------
	@echo --------------------------------------------------------------------------
	- pylint pigdicegame
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running flake8 -----------------------------
	@echo --------------------------------------------------------------------------
	- flake8 pigdicegame

lint:
	- pylint pigdicegame
	- flake8 pigdicegame

# Helpers -----------------------------------------------------------------------------
cleanup:
	- rmdir /Q /S htmlcov
	- del .\.coverage
	- del .\*\__pycache__