import random
import os
from player import Player


class Bot(Player):
    """
    Class represents a a bot that is beeing
    inheritanced by the Player class.
    """

    def __init__(self, username):
        """Class contrctor: If no username is given, it will generate one"""
        if username is None:
            username = self.get_random_botname(
                os.path.dirname(os.path.realpath(__file__)) +
                "\\resources\\botnames.txt")
        Player.__init__(self, username)

    def calculate_amount_of_throws(self):
        """Decide how many throws the bot wants to do"""
        odds = 1/6
        how_many_throws = 0
        while True:
            chance = int(100 * (odds * how_many_throws)) + 100
            if random.randint(0, chance) <= 100:
                how_many_throws += 1
            else:
                return how_many_throws

    def get_dice_throws(self):
        """Bot throws dices and return the points"""
        points = 0
        for dice_throws in range(self.calculate_amount_of_throws()):
            dice = self.throw_dice()
            if dice == 1:
                return 0
            points += dice
            if self.want_to_bank(points, dice_throws):
                return points
        return points

    def want_to_bank(self, total_points, dice_throws):
        """Checks if the bot wants to bank its points."""
        return dice_throws >= 2 and total_points > dice_throws * 3

    def get_random_botname(self, path):
        """Retrive a random bot name"""
        try:
            with open(path, "r") as file:
                names = file.readlines()
                return names[random.randint(0, len(names) - 1)].strip('\n')
        except FileNotFoundError as e:
            raise FileNotFoundError from e
