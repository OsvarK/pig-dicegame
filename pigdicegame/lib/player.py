import random
from userInterface import UserInterface


class Player(object):
    """ Class represents a player. """
    def __init__(self, username):
        super().__init__()
        self.score = 0
        self.username = username
        self.wins = 0
        self.higest_score_in_one_turn = []
        self.fastest_win = 0

    def throw_dice(self):
        """Throws the dice"""
        dice = random.randint(1, 6)
        UserInterface.display_dice_throw(self, dice)
        return dice

    def load_data(self):
        """Fetch data from storage"""
        # TODO: Get data from storage, and update this variables

    def save_data(self):
        """Save data to storage"""
        # TODO: save data to storage

    def is_higest_score_in_one_turn(self, new_higescore):
        """Check if this is the new higescore in one turn"""
        if sum(new_higescore) > sum(self.higest_score_in_one_turn):
            self.higest_score_in_one_turn = new_higescore

    def is_fastest_win(self, on_turn):
        """Check if this is the fastes win"""
        if on_turn < self.fastest_win:
            self.fastest_win = on_turn

    def i_win(self, on_turn):
        """This player won the game"""
        print(self.username + f" winns the game in {on_turn} turns!")
        self.wins += 1
        self.is_fastest_win(on_turn)
