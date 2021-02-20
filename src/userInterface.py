class UserInterface():
    """
    This class controlls the input and output to the player.

    Methods
    -------
        throwDiceQuestion(): int
            Asks the user to throw a dice
    """

    def __init__(self):
        super().__init__()

    def DisplayThrowDiceQuestion(self, firstTime):
        # TODO: Ask if player wants to throw dice
        # return, true / false
        return True

    def DisplayMainMenu(self):
        """Menu"""
        # Huvudmeny
        pass

    def DisplayGameStartup(self):
        """Maybe some startup stuffs"""
        # set how many players and bots osv...
        pass

    def DisplayWhosTurn(self, player):
        """Display whos turn it is"""
        # Varje turn så måste vi veta vems turn det är
        pass

    def displayDiceThrow(self, player, dice):
        """Display a dice throw"""
        # När ett throw händer vissa det.
        pass
