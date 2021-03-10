import unittest
import sys

sys.path.append("pigdicegame/lib")

import highscore
import player


class TestHighscore(unittest.TestCase):
#    # TODO: Skriv testkod för highscore
    def test_load_players(self):
        """Tests create_highscore()"""
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



        """
        player1 = Player("Swezoo")
        player1.fastestWin = 2
        player1.higestScoreInOneTurn = 60
        player1.fastestWin = 4
        scores.players.append(player1)
        player2 = Player("Sancla")
        player2.fastestWin = 112
        player2.higestScoreInOneTurn = []
        player2.fastestWin = 12354
        scores.players.append(player2)
        print(scores.highscore)
        print(scores.players)
        print("finished")
        scores.createHighScore()

        player = Player("Tester")
        player.higest_score_in_one_turn = 10
        player.is_higest_score_in_one_turn(20)
        self.assertTrue(p)
        player.higest_score_in_one_turn = 10
        player.is_higest_score_in_one_turn(5)
        self.assertTrue
        (player.higest_score_in_one_turn, 10)
        """
