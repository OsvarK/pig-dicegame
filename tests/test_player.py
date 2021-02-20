import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):

    def test_throwDice(self):
        """Tests Player:throwDice"""
        player = Player("Tester")
        for i in range(1, 20):
            self.assertTrue(player.throwDice() in range(1, 6))


# Run unitest, can also be runnned by 'py -m unititest test_player.py'
if __name__ == '__main__':
    unittest.main()
