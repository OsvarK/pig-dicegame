from src.player import Player


class Human(Player):
    """
    This class controlls the input and output to the player.

    Methods
    -------
        throwDiceQuestion(): int
            Asks the user to throw a dice
    """

    def __init__(self):
        super().__init__()

    def throwDiceQuestion(self, firstTime):
        """ Asks the user to throw dice or not

            Attribute:
                firsTime : bool
                determine if its the first time
                this question has been asked to this user.

            Return : int
        """

        # Todo: return dice throw, also check if player want to throw dice.
        # If player dont want to throw dice, return -1

        return 1
