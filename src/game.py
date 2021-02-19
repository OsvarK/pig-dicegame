from src.userInterface import UserInterface
class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.

    Attributes:
    -----------
        players : list of Player Classes
            A list of Player classes.
            List lenght: 1-4

    Methods
    -------
        gameLoop():
            This method controlls the flow of the game.
        startGame():
            This method starts the game.
        diceThrowLoop(): int
            This method controlls the flow of dice loop of the game.
        hasPlayerWon(Player): bool
            Determine if player has won.
        updateTurnIndex(int): int
            Determines whos turn it is, represented by an index.
        GameOver():
            Method to end game.
    """

    def __init__(self, players):
        """ Constructs the necessary logic needed to run the game """
        self.__players = players
        self.__ui = UserInterface()
        self.__gameIsActive = False

    def startGame(self):
        self.__gameIsActive = True
        self.__gameLoop()

    def __gameLoop(self):
        """ This fucntion controlls the flow of the game (the game loop) """
        turnIndex = 0
        while self.__gameIsActive:
            player = self.__players[turnIndex]      # Refreance current player.
            points = self.diceThrowLoop()           # player throw dice.
            player.addScore(points)                 # add score to player.
            turnIndex = self.updateTurnIndex()      # update turn index.
            if self.hasPlayerWon(player):           # check if player has won.
                self.GameOver(player)
                break

    def diceThrowLoop(self):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        firstThrow = True
        points = 0
        while True:
            dice = self.__ui.throwDiceQuestion(firstThrow)
            firstThrow = False
            if dice == -1:
                # No dice thrown
                break
            elif dice == 1:
                # Dice equals 1, remove all points & end turn.
                points = 0
                break
            else:
                # Append dice number to points pool.
                points += dice
        return points

    def hasPlayerWon(self, player):
        """ Checks if player has >= 100 points """
        return player.getScore() >= 100

    def updateTurnIndex(self, turnIndex):
        """ Updates the turn index, to keep track on who's turn it is """
        if turnIndex == (len(self.__players) - 1):
            turnIndex = 0
        else:
            turnIndex += 1
        return turnIndex

    def GameOver(self, player):
        """ Method that handels logic on game over"""
        self.__gameIsActive = False
        pass