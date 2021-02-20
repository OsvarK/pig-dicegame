import unittest
from pigdicegame.player import Player


class TestPlayer(unittest.TestCase):

    def test_throwDice(self):
        """Tests Player:throwDice"""
        player = Player("Tester")
        for i in range(1, 20):
            self.assertTrue(player.throwDice() in range(0, 7))


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
