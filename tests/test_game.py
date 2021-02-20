import unittest
from src.game import Game


class TestGame(unittest.TestCase):

    def test_startGame(self):
        pass

    # add the gameloop to test? but how

    def test_updateTurnIndex(self):
        """Tests game:updateTurnIndex function"""
        game = Game({1, 2, 3, 4})
        self.assertEqual(game.updateTurnIndex(0), 1)
        self.assertEqual(game.updateTurnIndex(1), 2)
        self.assertEqual(game.updateTurnIndex(2), 3)
        self.assertEqual(game.updateTurnIndex(3), 0)

    def test_gameOver(self):
        pass


# Run unitest, can also be runnned by 'py -m unititest test_game.py'
if __name__ == '__main__':
    unittest.main()
