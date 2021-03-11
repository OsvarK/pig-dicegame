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
        self.save_data(os.path.dirname(os.path.realpath(__file__)) +
                      "\\resources\\LocalHighscore.json")

    def save_data(self, path):
        """Save data to storage"""
        try:
            with open(path, "w")as file:
                json.dump(self.highscore, file, indent=2)
        except FileNotFoundError as e:
            print("Error: File not found")
        except json.JSONDecodeError:
            pass

    def load_data(self, path):
        """Fetch data from storage"""
        try:
            with open(path, "r")as file:
                self.highscore = json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError from e
        except json.JSONDecodeError:
            pass

    def create_players(self):
        """ Creates players from the loaded data.
            Needs to be called as the game starts
        """
        self.load_data(os.path.dirname(os.path.realpath(__file__)) +
                      "\\resources\\LocalHighscore.json")
        for entry in self.highscore:
            player = Player(entry["username"])
            player.score = entry["score"]
            player.higest_score_in_one_turn = entry["higest_score_in_one_turn"]
            player.fastest_win = entry["fastest_win"]
            self.players.append(player)

    def show_highscore(self):
        """ Prints the current highscore """
        if not self.players: 
            self.create_players()
        sorted_list = sorted(self.players, key = lambda player: player.score)
        print("\n***** Highscore *****\n")
        for entry in sorted_list:
            print(f"{entry.username}, Score: {entry.score}")
        print("\n*********************\n")
        
