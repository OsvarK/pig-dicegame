import random


class Bot:
    def __init__(self):
        pass

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
