import unittest
from src.bot import Bot


class TestBot(unittest.TestCase):

    def test_calculateHowManyThrows(self):
        """Tests bot:calculateHowManyThrows function"""
        bot = Bot(None)
        for x in range(1, 20):
            y = bot.calculateHowManyThrows()
            self.assertTrue(y >= 1)

    def test_getDiceThrows(self):
        """Tests bot:getDiceThrows function"""
        b = Bot()
        for i in range(0, 20):
            self.assertTrue(b.getDiceThrows(None) > 1)


# Run unitest, can also be runnned by 'py -m unititest test_boy.py'
if __name__ == '__main__':
    unittest.main()
