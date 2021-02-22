VENV = .venv/Scripts/

PYTHON:
	$(venv)python

PIP:
	PYTHON $(venv)pip

# Install ----------------------------------------------------
venv:
	@echo Creating a virtual environment...
	python3 -m venv .venv
	@echo virtual environment was created!
	@echo Now activate the virtual environment: '.venv/Scripts/activate'
	@echo To install requirements after activation: 'make install'

install:
	@echo Installing requirements.txt...
	PIP install -r requirements.txt

# Testing ----------------------------------------------------
unittest:
	- PYTHON -m unittest discover pigdicegame/tests

coverage:
	- coverage run -m unittest discover pigdicegame/tests
	- coverage html
	- coverage report -m

pylint:
	- pylint pigdicegame/lib

flake8:
	- flake8 pigdicegame/lib

test:
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running unittest----------------------------
	@echo --------------------------------------------------------------------------
	- PYTHON -m unittest discover pigdicegame/tests
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running coverage ---------------------------
	@echo --------------------------------------------------------------------------
	- coverage run -m unittest discover pigdicegame/tests
	- coverage html
	- coverage report -m
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running pylint -----------------------------
	@echo --------------------------------------------------------------------------
	- pylint pigdicegame/lib
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running flake8 -----------------------------
	@echo --------------------------------------------------------------------------
	- flake8 pigdicegame/lib

lint:
	- pylint pigdicegame/lib
	- flake8 pigdicegame/lib