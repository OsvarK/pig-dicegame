import unittest
import sys

sys.path.append("pigdicegame/lib")

import highscore
import player


class TestHighscore(unittest.TestCase):
    def test_load_players(self):
        """Tests create_players()"""
        scores = highscore.Highscore()
        self.assertIsInstance(scores, highscore.Highscore)
        player1 = player.Player("Swezoo")
        self.assertIsInstance(player1, player.Player)
        player1.wins = 2
        player1.higest_score_in_one_turn = 60
        player1.fastest_win = 4
        scores.players.append(player1)
        scores.create_highscore()
        scores.create_players()
        for profile in scores.players:
            if profile.username.lower() == "Swezoo":
                self.assertTrue(profile.score == 2)
                self.assertTrue(profile.higest_score_in_one_turn == 60)
                self.assertTrue(profile.fastest_win["fastest_win"] == 4)

    def test_throw_exception_load_data(self):
        """Tests highscore.load_data"""
        h = highscore.Highscore()
        with self.assertRaises(FileNotFoundError):
            h.load_data("test.txt")
            
    def test_see_highscore(self):
        scores = highscore.Highscore()
        value = scores.show_highscore()
        self.assertTrue(value, "Failed: show_highscore")