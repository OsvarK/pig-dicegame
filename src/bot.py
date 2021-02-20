import random
from src.player import Player


class Bot(Player):
    """
    Class represents a a bot that is beeing
    inheritanced by the Player class.

    Methods
    -------
        calculateHowManyThrows(): int
            calculate how many thros the bot are willing to do.
    """

    def __init__(self):
        super().__init__()
        self.calculateHowManyThrows()

    def calculateHowManyThrows(self):
        """Decide how many throws the bot wants to do"""
        odds = 1/6
        howManyThrows = 0
        while True:
            chance = int(100 * (odds * howManyThrows)) + 100
            if random.randint(0, chance) <= 100:
                howManyThrows += 1
            else:
                break
        return howManyThrows

    def getDiceThrows(self, ui):
        """
        Bot throws dices and returns points
        """
        points = 0
        for i in range(len(self.calculateHowManyThrows())):
            dice = self.throwDice()
            ui.displayDiceThrow(self, dice)
            if dice == 1:   # Dice landed one 1, return 0 points
                return 0
            points += dice
        return points
