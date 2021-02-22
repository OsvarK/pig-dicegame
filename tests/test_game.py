import sys
import unittest
sys.path.append("pigdicegame/lib")

from bot import Bot
from game import Game


class TestGame(unittest.TestCase):

    def test_BotGame(self):
        players = [
            Bot(),
            Bot(),
            Bot(),
            Bot()
        ]
        Game.startGame(players)


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
