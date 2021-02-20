import random


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
        super.__init__()
        self.score = 0
        self.username = username
        self.wins = 0
        self.higestScoreInOneTurn = []
        self.fastestWin = []

    def throwDice(self):
        """Throws the dice"""
        return random.Randomint(1, 6)

    def fetchData(self):
        """Fetch data from storage"""
        self.wins = 0
        self.higestScoreInOneTurn = []
        self.fastestWin = []
        pass

    def ishigestScoreInOneTurn(self, newHigescore):
        """Check if this is the new higescore in one turn"""
        pass

    def isfastestWin(self, onTurn):
        """Check if this is the fastes win"""
        pass

    def playerWon(self, onTurn):
        """This player won the game"""
        self.win += 1
        self.isfastestWin(onTurn)
