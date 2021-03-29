# Pig, the dice game
Pig is a simple dice game which in its basic form is playable with just a single die. You win by being the first player to score 100 or more points.

## Run the game
Open main.py using python; example:
```
python pigdicegame/lib/main.py
```
## Bots intelligence / risk factor
##### Our bots uses a simple risk factor:
First the bot makes a simulation of its upcomming throws. Thhe more it throws the dice the higer change to stop throwing, this can be adjusted using the **self.risk_factor** integer.
```py
        odds = 1/6 * self.risk_taker
        how_many_throws = 0
        while True:
        chance = int(100 * (odds * how_many_throws)) + 100
        if random.randint(0, chance) <= 100:
            how_many_throws += 1
        else:
            return how_many_throws
```

When the its makes its *real* throws the bot also decides if it wants to bank its points if its points is greater then half of the possible points that could have been gathered. We can also increase its risk here to with the **self.risk_factor** integer.
```py
if dice_throws >= 2 and total_points > (dice_throws * 3) + self.risk_taker:
```

#### Cheat
Type fusk instead of throwing the dice.

## Setup & installation using virtual environment.
#### Step 1 - Setting up the virtual environment
Open a terminal in the projects location *(same location as the makefile)*. Then insert the command below.
```
make venv
```
#### Step 2 - Activate the virtual environment
After setup is completed, activate the virtual environment.
```
.venv/Scripts/activate
```
if you are using powershell and the command dident work, use this command instead:
```
.venv/Scripts/Activate.ps1
```
#### Step 3 - Installation
Now install everything that is required.
```
make install
```
## Makefile commands.
A collection of all the commands in the makefile, for easy use.
| Command | Description |
| -------------|-------------|
| make venv | Creates a virtual environment |
| make install | Installs all the necessary packages from requirements.txt |
| make unittest | Runs all unittests |
| make coverage | Runs & gets a coverage report from all unittests |
| make pylint | Runs pylint |
| make flake8 | Runs flake8 |
| make test | Runs all tests and all linters |
| make lint | Runs all linters (flake8 & pylint) |
| make doc | Generates documentation using pydoc |
| make uml | Generates uml using pyreverse |
| make clean | Cleaning up the project folder |

## Generating UML & Documentation.
#### Docummentation
Generating the documentation is quite simple,
make sure you have 'make' installed, then just run the command below
```
make doc
```
#### UML
Generating the UML is a bit more difficult as we require graphviz, instruction on how to install graphviz can be found [here!](https://pygraphviz.github.io/documentation/latest/install.html). When you have graphviz installed just run the command below.
```
make uml
```

## Windows user having problem?
If you are a windows user, I recommend downloading [chocolatey](https://chocolatey.org/install) to make the whole process easier!
When you have chocolatey installed you can easily install graphviz and make.
```
choco install make
choco install graphviz
```

#### Application is built for windows, havent been tested on linux
