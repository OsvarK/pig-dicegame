import random
from userInterface import User_interface


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
        User_interface.display_dice_throw(self, dice)
        return dice

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
        self.wins += 1
        self.is_fastest_win(on_turn)
