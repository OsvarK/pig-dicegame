class User_interface():
    """
    This class controlls the input and output to the player.
    """

    @staticmethod
    def start():
        """Start of program"""
        # Entry point fom main.py
        pass

    @staticmethod
    def throw_dice_loop(player):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        # TODO: Make it possible to throw dice
        # and the logic to return points
        # return the points as a list
        return True

    @staticmethod
    def display_whos_turn(player):
        """Display whos turn it is"""
        print("New turn: " + player.username)
        # Varje turn så måste vi veta vems turn det är
        pass

    @staticmethod
    def display_dice_throw(player, dice):
        """Display a dice throw"""
        print(player.username + f" rolled: {dice}")
        pass
