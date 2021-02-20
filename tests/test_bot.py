import unittest
import os
from pigdicegame.bot import Bot


class TestBot(unittest.TestCase):

    def test_calculateHowManyThrows(self):
        """Tests bot:calculateHowManyThrows function"""
        bot = Bot()
        for x in range(1, 200):
            y = bot.calculateHowManyThrows()
            self.assertTrue(y >= 1)

    def test_getDiceThrows(self):
        """Tests bot:getDiceThrows function"""
        b = Bot()
        for i in range(0, 20):
            self.assertTrue(b.getDiceThrows() >= 0)

    def test_getRandomBotName(self):
        """Tests bot:getRandomBotName function"""
        b = Bot()
        PATH = os.path.dirname(os.path.realpath(__file__))
        with self.assertRaises(FileNotFoundError):
            b.getRandomBotName(PATH + "\\resources\\namebotsss.txt")
        for i in range(0, 20):
            self.assertTrue(isinstance(
                PATH +
                "\\resources\\botnames.txt", str)
            )


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
