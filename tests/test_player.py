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
        player = Player("Tester")
        player.ishigestScoreInOneTurn([5, 5, 5, 6])
        scoreSum = sum(player.higestScoreInOneTurn)
        self.assertTrue(player.higestScoreInOneTurn == [5, 5, 5, 6])
        self.assertTrue(scoreSum == sum([5, 5, 5, 6]))
        player.ishigestScoreInOneTurn([5, 2, 6])
        scoreSum = sum(player.higestScoreInOneTurn)
        self.assertFalse(player.higestScoreInOneTurn == [5, 2, 6])
        self.assertFalse(scoreSum == sum([5, 2, 6]))

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
        player = Player("Tester")
        player.wins = 10
        player.iWin(99)
        self.assertTrue(player.wins == 11)
