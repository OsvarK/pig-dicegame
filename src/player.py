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

    def throwDice(self):
        return random.Randomint(1, 6)
