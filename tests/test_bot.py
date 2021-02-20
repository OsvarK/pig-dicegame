import unittest
from src.bot import Bot


class TestBot(unittest.TestCase):

    def test_calculateHowManyThrows(self):
        """Tests bot:calculateHowManyThrows function"""
        bot = Bot()
        for x in range(1, 20):
            y = bot.calculateHowManyThrows()
            self.assertTrue(y >= 1)

    def test_getDiceThrows(self):
        """Tests bot:getDiceThrows function"""
        b = Bot()
        for i in range(0, 20):
            self.assertTrue(b.getDiceThrows(None) >= 0)

    def test_getRandomBotName(self):
        """Tests bot:getRandomBotName function"""
        b = Bot()
        for i in range(0, 20):
            result = b.getRandomBotName()
            self.assertTrue(isinstance(result, str))


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
