import json


class Highscore():

    def __init__(self):
        self.highscore = []
        self.player = []

    def loadData(self):
        """Fetch data from storage"""
        try:
            with open("LocalHighscore.json", "r") as file:
                self.highscore = json.load(file)
        except FileNotFoundError:
            print("Error: File not found")

    def saveData(self):
        print("saveData")
        """Save data to storage"""
        # TODO: save data to storage
        try:
            with open("LocalHighscore.json", "w") as file:
                json.dump(self.highscore, file, indent=2)
        except FileNotFoundError:
            print("Error: File Not Found")
