import sys
import unittest
sys.path.append("pigdicegame/lib")

from bot import Bot
from game import Game


class TestGame(unittest.TestCase):

    def test_BotGame(self):
        players = []
        players.append(Bot("Tester 1"))
        self.assertFalse(Game.start_game(players))
        for i in range(2, 5):
            players.append(Bot(f"Tester {i}"))
        self.assertTrue(Game.start_game(players))
        players.append(Bot("Tester 5"))
        self.assertFalse(Game.start_game(players))
