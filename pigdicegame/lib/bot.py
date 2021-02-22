import random
import os
from player import Player


class Bot(Player):
    """
    Class represents a a bot that is beeing
    inheritanced by the Player class.
    """

    def __init__(self, username):
        if username is None:
            username = self.getRandomBotName(
                os.path.dirname(os.path.realpath(__file__)) +
                "\\resources\\botnames.txt"
            )
        Player.__init__(self, username)

    def calculateHowManyThrows(self):
        """Decide how many throws the bot wants to do"""
        odds = 1/6
        howManyThrows = 0
        while True:
            chance = int(100 * (odds * howManyThrows)) + 100
            if random.randint(0, chance) <= 100:
                howManyThrows += 1
            else:
                return howManyThrows

    def getDiceThrows(self):
        """Bot throws dices and return the points"""
        points = 0
        for diceThrows in range(self.calculateHowManyThrows()):
            dice = self.throwDice()
            if dice == 1:   # Dice landed one 1, return 0 points
                return 0
            points += dice
            if (self.wantToBank(points, diceThrows)):
                return points
        return points

    def wantToBank(self, totalPoints, diceThrows):
        """Checks if the bot wants to bank its points."""
        return diceThrows >= 2 and totalPoints > diceThrows * 3

    def getRandomBotName(self, path):
        """Retrive a random bot name"""
        try:
            with open(path, "r") as file:
                names = file.readlines()
                return "[Bot] " + names[random.randint(0, len(names) - 1)].strip('\n')
        except FileNotFoundError:
            raise FileNotFoundError
