from player import Player
from userInterface import UserInterface
import unittest
import sys
import unittest.mock
from unittest.mock import patch
import test_highscore

sys.path.append("pigdicegame/lib")


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

    @patch('builtins.input', side_effect=["2", "Tomas", "3", "1", "Tomas", "Jörgen", "1", "1", "Jörgen", "1", "1", "FUSK"])
    def test_game_session(self, mock_print):
        output = []
        UserInterface.start()
        #testgame.assert_called_with(print('Jörgen won the game!'))
        assert output == [
            "1. Play game \n" +
            "2. Create player profile \n" +
            "3. Change player profile \n" +
            "4. See highscore \n" +
            "5. Exit \n", "Hej"]
