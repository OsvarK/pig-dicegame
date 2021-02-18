import unittest
from src.userInterface import UserInterface


class TestUserInterface(unittest.TestCase):

    def test_throwDiceQuestion(self):
        """ Tests UserInterface:throwDiceQuestion"""
        ui = UserInterface()
        result = ui.throwDiceQuestion(True)
        self.assertTrue(result in range(-1, 6))


# Run unitest, can also be runnned by 'py -m unititest test_userInterface.py'
if __name__ == '__main__':
    unittest.main()
