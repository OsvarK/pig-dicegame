import random
from pigdicegame.game import Game


class Player(object):
    """
    Class represents a player.

    Methods
    -------
        addScore(int): int
            adds score to player, then returns that score
        getScore(): int
            retrive score from player.
        throwDice(): int
            throws dice.
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
        Game.getInstance().ui.displayDiceThrow()
        return random.randint(1, 6)

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
        self.win += 1
        self.isfastestWin(onTurn)
