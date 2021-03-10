import sys
import unittest
sys.path.append("pigdicegame/lib")

from bot import Bot
import userInterface
import game


class TestGame(unittest.TestCase):

    def test_BotGame(self):
        the_game = game.Game(userInterface.UserInterface)
        players = []
        players.append(Bot("Tester 1", 1))
        self.assertFalse(the_game.start_game(players))
        for i in range(2, 5):
            players.append(Bot(f"Tester {i}", 2))
        self.assertTrue(the_game.start_game(players))
        players.append(Bot("Tester 5", 3))
        self.assertFalse(the_game.start_game(players))
