import json


class Highscore():

    def __init__(self):
        self.highscore = []
        self.players = []

    def createHighScore(self):
        new_score = []
        for player in self.players:
            new_score.append(player.__dict__)
        self.highscore = new_score
        self.saveData()

    def saveData(self):
        """Save data to storage"""
        try:
            with open("LocalHighscore.json", "w") as file:
                json.dump(self.highscore, file, indent=2)
        except FileNotFoundError:
            print("Error: File Not Found")

            
    def loadData(self):
        """Fetch data from storage"""
        try:
            with open("LocalHighscore.json", "r") as file:
                self.highscore = json.load(file)
        except FileNotFoundError:
            print("Error: File not found")
