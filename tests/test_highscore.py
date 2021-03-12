import unittest
import sys

sys.path.append("pigdicegame/lib")

import highscore
import player


class TestHighscore(unittest.TestCase):

    def test_save_data_add_player_to_save(self):
        score = highscore.Highscore()
        score.players.append(player.Player("Swezoo"))
        score.save_data("pigdicegame\\lib\\resources\\LocalHighscore.json")
        with self.assertRaises(FileNotFoundError):
            score.save_data("LocalHighscore.json")

    def test_exception_for_laod_data(self):
        score = highscore.Highscore()
        with self.assertRaises(FileNotFoundError):
            score.load_data("LocalHighscore.json")

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

    def test_see_highscore(self):
        scores = highscore.Highscore()
        value = scores.show_highscore()
        self.assertTrue(value, "Failed: show_highscore")

    def test_save_data_empty_save(self):
        score = highscore.Highscore()
        score.players.append(player.Player("Swezoo"))
        score.save_data("pigdicegame\\lib\\resources\\LocalHighscore.json")
        with self.assertRaises(FileNotFoundError):
            score.save_data("LocalHighscore.json")
