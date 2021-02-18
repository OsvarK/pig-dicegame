# player logic
class Player:
    """
    Class represents a player.

    Methods
    -------
        addScore(): int
            adds score to player, then returns that score
            return: int
        getScore():
            retrive score from player.
            return: int
    """

    def __init__(self):
        self.__score = 0

    def addScore(self, score):
        self.__score += score
        return self.getScore()

    def getScore(self):
        return self.__score
