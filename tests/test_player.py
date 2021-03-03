import unittest
import sys

sys.path.append("pigdicegame/lib")

from player import Player


class TestPlayer(unittest.TestCase):

    def test_throwDice(self):
        """Tests Player:throwDice"""
        player = Player("Tester")
        for i in range(1, 20):
            self.assertTrue(player.throwDice() in range(0, 7))

    def test_loadDate(self):
        pass

    def test_saveData(self):
        pass

    def test_ishigestScoreInOneTurn(self):
        pass

    def test_isfastestWin(self):
        player = Player("Tester")
        player.fastestWin = 10
        player.isfastestWin(12)
        self.assertFalse(player.fastestWin == 12)
        self.assertTrue(player.fastestWin == 10)
        player.isfastestWin(5)
        self.assertFalse(player.fastestWin == 10)
        self.assertTrue(player.fastestWin == 5)

    def test_iWin(self):
        pass
