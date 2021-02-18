import unittest
from src.game import Game
from src.player import Player


class TestGame(unittest.TestCase):

    def test_hasPlayerWon(self):
        """Tests game:hasPlayerWon function"""
        game = Game({1, 2, 3, 4})
        player = Player()
        self.assertFalse(game.hasPlayerWon(player))
        player.addScore(99)
        self.assertFalse(game.hasPlayerWon(player))
        player.addScore(1)
        self.assertTrue(game.hasPlayerWon(player))

    def test_updateTurnIndex(self):
        """Tests game:updateTurnIndex function"""
        game = Game({1, 2, 3, 4})
        self.assertEqual(game.updateTurnIndex(0), 1)
        self.assertEqual(game.updateTurnIndex(1), 2)
        self.assertEqual(game.updateTurnIndex(2), 3)
        self.assertEqual(game.updateTurnIndex(3), 0)


# Run unitest, can also be runnned by 'py -m unititest test_game.py'
if __name__ == '__main__':
    unittest.main()
