VENV = virtual_env/Scripts/

PYTHON:
	$(venv)python

PIP:
	PYTHON $(venv)pip

# Install ----------------------------------------------------
setup:
	@echo Creating a virtual environment...
	python3 -m venv virtual_env
	@echo virtual environment was created!
	@echo Uppgrading pip...
	PIP install --upgrade pip
	@echo Setup is complete!
	@echo Now activate the virtual environment: 'virtual_env/Scripts/activate'
	@echo after activation type 'make install'

install:
	@echo Installing requirements.txt...
	PIP install -r requirements.txt
	@echo installing the project... (this step is nessesary to run tests)
	PIP install .
	@echo All done, type pig for execution of application or run tests using: 'make test'

# Testing ----------------------------------------------------
test-unittest:
	- PYTHON -m unittest discover . "tests/test_*.py"

test-coverage:
	- coverage run -m unittest discover . "tests/test_*.py"
	- coverage html
	- coverage report -m

test-pylint:
	- pylint pigdicegame

test-flake8:
	- flake8 pigdicegame

test-all:
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running unittest----------------------------
	@echo --------------------------------------------------------------------------
	- PYTHON -m unittest discover . "tests/test_*.py"
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running coverage ---------------------------
	@echo --------------------------------------------------------------------------
	- coverage run -m unittest discover . "tests/test_*.py"
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

test-lint:
	- pylint pigdicegame
	- flake8 pigdicegame

