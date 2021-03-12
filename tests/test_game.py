import sys
import unittest
sys.path.append("pigdicegame/lib")

from bot import Bot
import userInterface
import game


class TestGame(unittest.TestCase):
    def test_bot_game(self):
        """Tests the whole game when its only runned by bots"""
        the_game = game.Game(userInterface.UserInterface)
        the_game.test_mode = True
        players = []
        bot = Bot("test_bot_game 1", 1)
        bot.test_mode = True
        players.append(bot)
        self.assertFalse(the_game.start_game(players))
        for i in range(2, 5):
            bot = Bot(f"test_bot_game {i}", 2)
            bot.test_mode = True
            players.append(bot)
        self.assertTrue(the_game.start_game(players))
        bot = Bot("test_bot_game 5", 3)
        bot.test_mode = True
        players.append(bot)
        self.assertFalse(the_game.start_game(players))
