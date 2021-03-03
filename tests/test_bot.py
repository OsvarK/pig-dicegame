import unittest
import os
import sys

sys.path.append("pigdicegame/lib")

from bot import Bot


class TestBot(unittest.TestCase):

    def test_calculate_amount_of_throws(self):
        """Tests bot:calculate_amount_of_throws function"""
        bot = Bot(None)
        for x in range(1, 200):
            y = bot.calculate_amount_of_throws()
            self.assertTrue(y >= 1)

    def test_get_dice_throws(self):
        """Tests bot:get_dice_throws function"""
        b = Bot(None)
        for i in range(0, 20):
            self.assertTrue(b.get_dice_throws() >= 0)

    def test_want_to_bank(self):
        """Tests bot:want_to_bank function"""
        b = Bot(None)
        self.assertTrue(b.want_to_bank(12, 2))
        self.assertTrue(b.want_to_bank(13, 4))
        self.assertTrue(b.want_to_bank(7, 2))
        self.assertFalse(b.want_to_bank(6, 2))
        self.assertFalse(b.want_to_bank(12, 4))
        self.assertFalse(b.want_to_bank(6, 1))

    def test_get_random_botname(self):
        """Tests bot:get_random_botname function"""
        b = Bot(None)
        with self.assertRaises(FileNotFoundError):
            b.get_random_botname("bot.txt")
        for i in range(0, 20):
            self.assertTrue(isinstance(
                "pigdicegame/resources/botnames.txt", str))
