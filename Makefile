VENV = virtual_env/Scripts/

# Python executable
PYTHON:
	$(venv)python


# pip executable
PIP:
	PYTHON $(venv)pip


# installation ---------------------------------------------------------------------------------
# Install virtual env
venv-setup:
	@echo Creating a virtual environment...
	python3 -m venv virtual_env
	@echo virtual environment was created!
	@echo Uppgrading pip...
	PIP install --upgrade pip
	@echo Setup is complete!
	@echo Now activate the virtual environment: 'virtual_env/Scripts/activate'
	@echo after activation type 'make venv-install'


# installing application, recomended to run 'make venv-setup' before.
venv-install:
	@echo Installing requirements.txt...
	PIP install -r requirements.txt
	@echo setting up the project...
	PIP install .
	@echo All done, type pig for execution of application.


