import unittest
import os
import sys

sys.path.append("pigdicegame/lib")

from bot import Bot


class TestBot(unittest.TestCase):

    def test_calculate_amount_of_throws(self):
        """Tests bot:calculate_amount_of_throws function"""
        bot = Bot(None, 1)
        for _ in range(1, 10):
            y = bot.calculate_amount_of_throws()
            self.assertTrue(y >= 1)
        bot = Bot(None, 2)
        for _ in range(1, 10):
            y = bot.calculate_amount_of_throws()
            self.assertTrue(y >= 1)
        bot = Bot(None, 3)
        for _ in range(1, 10):
            y = bot.calculate_amount_of_throws()
            self.assertTrue(y >= 1)

    def test_get_dice_throws(self):
        """Tests bot:get_dice_throws function"""
        b = Bot(None, 1)
        for _ in range(0, 20):
            self.assertTrue(b.get_dice_throws() >= 0)

    def test_want_to_bank(self):
        """Tests bot:want_to_bank function"""
        bot_level = 1
        bot = Bot("Tester1", bot_level)
        throws = 3
        self.assertTrue(bot.want_to_bank(20, throws), (throws * 3) + bot_level)
        bot_level = 2
        bot = Bot("Tester2", bot_level)
        throws = 5
        self.assertTrue(
            bot.want_to_bank(18, throws), (throws * 3) + bot_level)
        self.assertFalse(
            bot.want_to_bank(17, throws), (throws * 3) + bot_level)

    def test_get_random_botname(self):
        """Tests bot:get_random_botname function"""
        b = Bot(None, 1)
        with self.assertRaises(FileNotFoundError):
            b.get_random_botname("bot.txt")
        for _ in range(0, 20):
            self.assertTrue(isinstance(
                "pigdicegame/resources/botnames.txt", str))
