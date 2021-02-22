from userInterface import UserInterface
from bot import Bot


class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.
    """
    def startGame(self, players):
        """Takes list of players and starts the gameloop.
        Returns false if game was not able to be created
        """
        if len(players) > 1:
            self.__gameLoop(players)
            return True
        return False

    def __gameLoop(self, players):
        """This fucntion controlls the flow of the game (the game loop)"""
        playerIndex = 0
        turnCycle = 0
        while True:
            player = players[playerIndex]
            UserInterface.DisplayWhosTurn(player)
            if isinstance(player, Bot):
                points = self.botDiceLoop()
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
                self.GameOver(player)
                break

    def gameOver(self, player, turnCycle):
        """Fucntion to end the gameloop and declares a winner.
            arg1 (Player): the winner of the game.
            arg2 (int): on what turn cycle the game was ended.
        """
        player.iWin()
