import unittest
import os
import sys

sys.path.append("pigdicegame/lib")

from bot import Bot


class TestBot(unittest.TestCase):

    def test_calculateHowManyThrows(self):
        """Tests bot:calculateHowManyThrows function"""
        bot = Bot(None)
        for x in range(1, 200):
            y = bot.calculateHowManyThrows()
            self.assertTrue(y >= 1)

    def test_getDiceThrows(self):
        """Tests bot:getDiceThrows function"""
        b = Bot(None)
        for i in range(0, 20):
            self.assertTrue(b.getDiceThrows() >= 0)

    def test_wantToBank(self):
        b = Bot(None)
        self.assertTrue(b.wantToBank(12, 2))
        self.assertTrue(b.wantToBank(13, 4))
        self.assertTrue(b.wantToBank(7, 2))
        self.assertFalse(b.wantToBank(6, 2))
        self.assertFalse(b.wantToBank(12, 4))
        self.assertFalse(b.wantToBank(6, 1))

    def test_getRandomBotName(self):
        """Tests bot:getRandomBotName function"""
        b = Bot(None)
        with self.assertRaises(FileNotFoundError):
            b.getRandomBotName("bot.txt")
        for i in range(0, 20):
            self.assertTrue(isinstance(
                "pigdicegame/resources/botnames.txt", str))
