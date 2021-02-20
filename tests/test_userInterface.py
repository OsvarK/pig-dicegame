import unittest
from pigdicegame.userInterface import UserInterface


class TestUserInterface(unittest.TestCase):

    def test_throwDiceQuestion(self):
        """ Tests UserInterface:throwDiceQuestion"""
        ui = UserInterface()
        result = ui.throwDiceQuestion(True)
        self.assertTrue(result in range(-1, 6))


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
