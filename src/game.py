from UserInterface import UI


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
            This method is the flow of the game.
            This method is called on class construction.
    """

    def __init__(self, players):
        """ Constructs the necessary logic needed to run the game """
        self.__players = players
        self.__ui = UI()
        self.__gameIsActive = True
        self.__gameLoop()

    def __gameLoop(self):
        """ This fucntion controlls the flow of the game (game loop) """
        turnIndex = 0
        # Turn loop
        while(self.__gameIsActive):
            # init this turn
            player = self.__players[turnIndex]
            firstThrow = True
            points = 0
            # Throw dice loop
            while(True):
                # Throw dice
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
            # Add score to player
            player.addScore(points)
            # Check if the player has won
            if player.getScore() >= 100:
                self.__GameOver(player)
            # Get new turn index
            if turnIndex == len(self.__players):
                turnIndex = 0
            else:
                turnIndex += 1

    def __GameOver(self, player):
        """ Method that handels logic on game over"""
        self.__gameIsActive = False
        pass
