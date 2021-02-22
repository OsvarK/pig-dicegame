import random
import os
from player import Player


class Bot(Player):
    """
    Class represents a a bot that is beeing
    inheritanced by the Player class.
    """

    def __init__(self):
        super(Bot).__init__()
        self.username = self.getRandomBotName(
            os.path.dirname(os.path.realpath(__file__)) +
            "\\resources\\botnames.txt"
        )

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
        for i in range(self.calculateHowManyThrows()):
            dice = self.throwDice()
            if dice == 1:   # Dice landed one 1, return 0 points
                return 0
            points += dice
        return points

    def getRandomBotName(self, path):
        """Retrive a random bot name"""
        try:
            with open(path, "r") as file:
                names = file.readlines()
                return "[Bot] " + names[random.randint(0, len(names) - 1)]
        except FileNotFoundError:
            raise FileNotFoundError
