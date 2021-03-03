.ONESHELL:

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
	- PYTHON -m unittest discover tests

coverage:
	- rmdir coverage_results /s /q
	- coverage run -m unittest discover tests
	- coverage html
	- coverage report -m
	- mkdir coverage_results
	- move .coverage ./coverage_results
	- move htmlcov ./coverage_results

pylint:
	- pylint pigdicegame/lib

flake8:
	- flake8 pigdicegame/lib

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
	- pylint pigdicegame/lib
	@echo --------------------------------------------------------------------------
	@echo ----------------------------- Running flake8 -----------------------------
	@echo --------------------------------------------------------------------------
	- flake8 pigdicegame/lib

lint:
	- pylint pigdicegame/lib
	- flake8 pigdicegame/lib

doc:
	# Generating docks.
	# with an ugly solution, but it works.
	mkdir docs
	cd .\pigdicegame
	PYTHON -m pydoc -w .\main.py
	move .\main.html ..\docs
	cd .\lib
	PYTHON -m pydoc -w .\__init__.py
	move .\__init__.html ..\..\docs
	PYTHON -m pydoc -w .\bot.py
	move .\bot.html ..\..\docs
	PYTHON -m pydoc -w .\game.py
	move .\game.html ..\..\docs
	PYTHON -m pydoc -w .\player.py
	move .\player.html ..\..\docs
	PYTHON -m pydoc -w .\userInterface.py
	move .\userInterface.html ..\..\docs

uml:
	# Install 'pip install pylint' as admin in none venv.
	# Install 'choco install graphviz' as admin in none venv.
	pyreverse -o png .\pigdicegame\lib
	move .\packages.png .\docs
	move .\classes.png .\docs

clean:
	rmdir coverage_results /s /q
	rmdir .\pigdicegame\__pycache__ /s /q
	rmdir .\pigdicegame\lib\__pycache__ /s /q
	rmdir .\pigdicegame\lib\resources\__pycache__ /s /q
	rmdir .\tests\__pycache__ /s /q