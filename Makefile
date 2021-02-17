VENV = virtual_env/Scripts/

# Python executable
PYTHON:
	$(venv)python


# pip executable
PIP:
	PYTHON $(venv)pip


# installation ---------------------------------------------------------------------------------
# Install virtual env
setup:
	@echo Creating a virtual environment...
	python3 -m venv virtual_env
	@echo virtual environment was created!
	@echo Uppgrading pip...
	PIP install --upgrade pip
	@echo Setup is complete!
	@echo Now activate the virtual environment: 'virtual_env/Scripts/activate'
	@echo after activation type 'make install'


# installing application, recomended to run 'make setup' before.
install:
	@echo Installing requirements.txt...
	PIP install -r requirements.txt
	@echo installing the project... (this step is nessesary to run tests)
	PIP install .
	@echo All done, type pig for execution of application or run tests using: 'make test'


# Test all test files
test:
	PYTHON tests/test_bot.py
	PYTHON tests/test_game.py
	PYTHON tests/test_player.py
	PYTHON tests/test_userInterface.py


