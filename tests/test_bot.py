import unittest
from src.bot import Bot


class TestBot(unittest.TestCase):
    def calculateHowManyThrows(self):
        """Tests bbot:calculateHowManyThrows function"""
        bot = Bot()
        for x in range(1, 20):
            y = bot.calculateHowManyThrows()
            self.assertTrue(y >= 1)


# Run unitest, can also be runnned by 'py -m unititest test_boy.py'
if __name__ == '__main__':
    unittest.main()
