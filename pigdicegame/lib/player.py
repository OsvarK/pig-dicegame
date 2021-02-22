import random
from userInterface import UserInterface


class Player(object):
    """
    Class represents a player.
    """

    def __init__(self, username):
        super().__init__()
        self.score = 0
        self.username = username
        self.wins = 0
        self.higestScoreInOneTurn = []
        self.fastestWin = 0

    def throwDice(self):
        """Throws the dice"""
        dice = random.randint(1, 6)
        UserInterface.displayDiceThrow(self, dice)
        return dice

    def loadData(self):
        """Fetch data from storage"""
        # TODO: Get data from storage, and update this variables
        self.wins = 0
        self.higestScoreInOneTurn = []
        self.fastestWin = []

    def saveData(self):
        """Save data to storage"""
        # TODO: save data to storage

    def ishigestScoreInOneTurn(self, newHigescore):
        """Check if this is the new higescore in one turn"""
        if newHigescore > sum(self.higestScoreInOneTurn):
            self.higestScoreInOneTurn = newHigescore

    def isfastestWin(self, onTurn):
        """Check if this is the fastes win"""
        if onTurn < self.fastestWin:
            self.fastestWin = onTurn

    def iWin(self, onTurn):
        """This player won the game"""
        print(self.username + f" winns the game in {onTurn} turns!")
        self.wins += 1
        self.isfastestWin(onTurn)
