from pigdicegame.userInterface import UserInterface


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
        updateTurnIndex(int): int
            Determines whos turn it is, represented by an index.
        gameOver():
            Method to end game.
    """
    __instance = None

    @staticmethod
    def getInstance():
        """Retrive singletoon of this class"""
        if Game.__instance is None:
            Game()
        return Game.__instance

    def __init__(self):
        """ Constructs the necessary logic needed to run the game """
        # Create singleton
        if Game.__instance is None:
            Game.__instance = self
        # Set varaiables
        self.players = None
        self.ui = UserInterface()
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
        turnCycle = 0
        while self.__gameIsActive:

            # Refreance current player.
            player = self.__players[turnIndex]
            self.ui.DisplayWhosTurn(player)

            # Get points from either the player or the bot
            # (Maybe do this with if statements isntead?)
            try:
                # Bot throw dice
                points = self.botDiceLoop(self.ui)
            except Exception:
                pass
            else:
                # Player throw dice
                pointsAccumulated = self.ui.ThrowDiceLoop(player)
                player.ishigestScoreInOneTurn(pointsAccumulated)
                points = sum(pointsAccumulated)

            # Add score to player.
            player.score += points

            # Update turn
            if turnIndex == (len(self.players) - 1):
                turnIndex = 0
                turnCycle += 1
            else:
                turnIndex += 1

            # Check if player has won.
            if player.score >= 100:
                self.GameOver(player)
                break

    def gameOver(self, player, turn):
        """ Method that handels logic on game over"""
        self.__gameIsActive = False
        player.iWin()
