import unittest
import sys
import unittest.mock

sys.path.append("pigdicegame/lib")

from userInterface import UserInterface

class TestUserInterface(unittest.TestCase):
    # inspiration from user gawel at 
    # https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
    def test_input_handler_int_range_in_range(self):
        with unittest.mock.patch("builtins.input", return_value=2):
            assert UserInterface.input_handler_int_range("enter int", 1, 4) == 2     
            
        with unittest.mock.patch("builtins.input", return_value="a"):
            with self.assertRaises(ValueError):
                UserInterface.input_handler_int_range("enter int", 1, 4)