from src.userInterface import UserInterface


class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.

    Methods
    -------
        gameLoop():
            Method thats controlls the flow of the game.
        startGame(Players):
            Method to start the game.
        humanDiceLoop(): int
            This method controlls the flow of dice for the human.
        botDiceLoop(): int
            This method controlls the flow of dice for the bot.
        hasPlayerWon(Player): bool
            Determine if player has won.
        updateTurnIndex(int): int
            Determines whos turn it is, represented by an index.
        gameOver():
            Method to end game.
    """

    def __init__(self):
        """ Constructs the necessary logic needed to run the game """
        self.players = None
        self.__ui = UserInterface()
        self.__gameIsActive = False

    def startGame(self, Players):
        """ Starts the game, param = list of players """
        self.players = Players
        self.__gameIsActive = True
        self.__gameLoop()

    def __gameLoop(self):
        """ This fucntion controlls the flow of the game (the game loop) """
        # Keep track on whos turn it is.
        turnIndex = 0
        while self.__gameIsActive:

            # Refreance current player.
            player = self.__players[turnIndex]
            self.__ui.DisplayWhosTurn(player)

            # Get points from either the player
            # or the bot, (Maybe do this with if statements isntead?)
            try:
                points = self.botDiceLoop(self.__ui)
            except Exception:
                pass
            else:
                points = self.__ui.ThrowDiceLoop(player)

            player.score += points                  # Add score to player.
            turnIndex = self.updateTurnIndex()      # Update turn index.
            if self.hasPlayerWon(player):           # Check if player has won.
                self.GameOver(player)
                break

    def hasPlayerWon(self, player):
        """ Checks if player has >= 100 points """
        return player.score >= 100

    def updateTurnIndex(self, turnIndex):
        """ Updates the turn index, to keep track on who's turn it is """
        if turnIndex == (len(self.players) - 1):
            turnIndex = 0
        else:
            turnIndex += 1
        return turnIndex

    def gameOver(self, player):
        """ Method that handels logic on game over"""
        self.__gameIsActive = False
        # TODO: Add logic
