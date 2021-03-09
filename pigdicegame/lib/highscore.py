"""
Module to handle everything connected to data for highscores
"""

import os
import json
from player import Player


class Highscore():
    """
    Class represents a the data for highscore and list of players.
    """

    def __init__(self):
        self.highscore = []
        self.players = []

    def create_highscore(self):
        """ Converts the list of player-object to JSON
        format and calls to save the data.
        Needs to be called before the game is closed.
        """
        new_score = []
        for player in self.players:
            new_score.append(player.__dict__)
        self.highscore = new_score
        self.save_data()

    def save_data(self):
        """Save data to storage"""
        try:
            with open(os.path.dirname(os.path.realpath(__file__)) +
                      "\\resources\\LocalHighscore.json", "w")as file:
                json.dump(self.highscore, file, indent=2)
        except FileNotFoundError:
            print("Error: File Not Found")
        except json.JSONDecodeError:
            pass

    def load_data(self):
        """Fetch data from storage"""
        try:
            with open(os.path.dirname(os.path.realpath(__file__)) +
                      "\\resources\\LocalHighscore.json", "r")as file:
                self.highscore = json.load(file)
        except FileNotFoundError:
            print("Error: File not found")
        except json.JSONDecodeError:
            pass

    def create_players(self):
        """ Creates players from the loaded data.
            Needs to be called as the game starts
        """
        self.load_data()
        for entry in self.highscore:
            player = Player(entry["username"])
            player.score = entry["score"]
            player.higest_score_in_one_turn = entry["higest_score_in_one_turn"]
            player.fastest_win = entry["fastest_win"]
            self.players.append(player)
