import unittest
import sys
import unittest.mock
from unittest.mock import patch

sys.path.append("pigdicegame/lib")

from userInterface import UserInterface
from player import Player


class TestUserInterface(unittest.TestCase):
    # inspiration from user gawel at 
    # https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
    def test_input_handler_int_range_in_range(self):
        with unittest.mock.patch("builtins.input", return_value=2):
            assert UserInterface.input_handler_int_range(
                "enter int", 1, 4) == 2

        with unittest.mock.patch("builtins.input", return_value="a"):
            with self.assertRaises(ValueError):
                UserInterface.input_handler_int_range("enter int", 1, 4)

    def test_throw_dice_loop(self):
        """Unittest for UI:throw_dice_loop"""
        ply = Player("throw_dice_loop_tester")
        with unittest.mock.patch("builtins.input", side_effect=[
                                 "Y", "Y", "Y", "N"]):
            self.assertIsInstance(UserInterface.throw_dice_loop(ply), int)