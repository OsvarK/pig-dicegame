class UserInterface():
    """
    This class controlls the input and output to the player.

    Methods
    -------
        throwDiceLoop(Player): int
            Logic to controll the dice loop for the user.
        displayMainMenu():
            Display main menu.
        displayGameStartup():
            Display game setup.
        displayWhosTurn(Player):
            Display whos turn it is, when a new turn in the game occures.
        displayDiceThrow(Player, dice):
            Display a dice throw
    """

    def __init__(self):
        super().__init__()

    def throwDiceLoop(self, player):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        # TODO: Make it possible to throw dice
        # and the logic to return points
        # return the points
        return True

    def displayMainMenu(self):
        """Menu"""
        # Huvudmeny
        pass

    def displayGameStartup(self):
        """Maybe some startup stuffs"""
        # set how many players and bots osv...
        pass

    def displayWhosTurn(self, player):
        """Display whos turn it is"""
        # Varje turn så måste vi veta vems turn det är
        pass

    def displayDiceThrow(self, player, dice):
        """Display a dice throw"""
        # När ett throw händer vissa det.
        pass
