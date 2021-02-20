from pigdicegame.userInterface import UserInterface
from pigdicegame.bot import Bot


class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.
    """
    __instance = None

    @staticmethod
    def getInstance():
        """Retrives the singletoon of this class.
        If there is no singleton, create one
        """
        if Game.__instance is None:
            Game()
        return Game.__instance

    def __init__(self):
        """Class constructor, set singleton and default variables"""
        if Game.__instance is None:
            Game.__instance = self
        self.ui = UserInterface()

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
            self.ui.DisplayWhosTurn(player)
            if isinstance(player, Bot):
                points = self.botDiceLoop(self.ui)
            else:
                pointsAccumulated = self.ui.ThrowDiceLoop(player)
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
