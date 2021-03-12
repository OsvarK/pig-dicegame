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

    @patch('builtins.input', side_effect=["Y", "Y", "Y", "N"])
    def test_throw_dice_loop(self, mock_print):
        """Unittest for UI:throw_dice_loop"""
        ply = Player("throw_dice_loop_tester")
        self.assertIsInstance(UserInterface.throw_dice_loop(ply), int)

    @patch('builtins.print')
    def test_display_whos_turn(self, mock_print):
        ply = Player("joe")
        UserInterface.display_whos_turn(ply)
        mock_print.assert_called_with("New turn: " + ply.username)