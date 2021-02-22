from userInterface import UserInterface
from bot import Bot


class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.
    """
    @staticmethod
    def startGame(players):
        """Takes list of players and starts the gameloop.
        Returns false if game was not able to be created
        """
        if len(players) in range(2, 5):
            Game.__gameLoop(players)
            return True
        return False

    @staticmethod
    def __gameLoop(players):
        """This function controlls the flow of the game (the game loop)
        arg (list:player): list of players
        """
        playerIndex = 0
        turnCycle = 0
        while True:
            player = players[playerIndex]
            UserInterface.displayWhosTurn(player)
            if isinstance(player, Bot):
                points = player.getDiceThrows()
            else:
                pointsAccumulated = UserInterface.throwDiceLoop(player)
                player.ishigestScoreInOneTurn(pointsAccumulated)
                points = sum(pointsAccumulated)
            player.score += points
            if playerIndex == (len(players) - 1):
                playerIndex = 0
                turnCycle += 1
            else:
                playerIndex += 1
            if player.score >= 100:
                Game.gameOver(player, turnCycle)
                break

    @staticmethod
    def gameOver(player, turnCycle):
        """Fucntion to end the gameloop and declares a winner.
            arg1 (Player): the winner of the game.
            arg2 (int): on what turn cycle the game was ended.
        """
        player.iWin(turnCycle)
