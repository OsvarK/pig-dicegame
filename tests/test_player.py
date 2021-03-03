import unittest
import sys

sys.path.append("pigdicegame/lib")

from player import Player


class TestPlayer(unittest.TestCase):

    def test_throw_dice(self):
        """Tests Player:throwDice"""
        player = Player("Tester")
        for i in range(1, 20):
            self.assertTrue(player.throw_dice() in range(0, 7))

    def test_load_date(self):
        pass

    def test_save_data(self):
        pass

    def test_is_higest_score_in_one_turn(self):
        player = Player("Tester")
        player.is_higest_score_in_one_turn([5, 5, 5, 6])
        scoreSum = sum(player.higest_score_in_one_turn)
        self.assertTrue(player.higest_score_in_one_turn == [5, 5, 5, 6])
        self.assertTrue(scoreSum == sum([5, 5, 5, 6]))
        player.is_higest_score_in_one_turn([5, 2, 6])
        scoreSum = sum(player.higest_score_in_one_turn)
        self.assertFalse(player.higest_score_in_one_turn == [5, 2, 6])
        self.assertFalse(scoreSum == sum([5, 2, 6]))

    def test_is_fastest_win(self):
        player = Player("Tester")
        player.fastest_win = 10
        player.is_fastest_win(12)
        self.assertFalse(player.fastest_win == 12)
        self.assertTrue(player.fastest_win == 10)
        player.is_fastest_win(5)
        self.assertFalse(player.fastest_win == 10)
        self.assertTrue(player.fastest_win == 5)

    def test_i_win(self):
        player = Player("Tester")
        player.wins = 10
        player.i_win(99)
        self.assertTrue(player.wins == 11)
