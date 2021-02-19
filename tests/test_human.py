import unittest
from src.human import Human


class TestHuman(unittest.TestCase):

    def test_throwDiceQuestion(self):
        """ Tests UserInterface:throwDiceQuestion"""
        ui = Human()
        result = ui.throwDiceQuestion(True)
        self.assertTrue(result in range(-1, 6))


# Run unitest, can also be runnned by 'py -m unititest test_userInterface.py'
if __name__ == '__main__':
    unittest.main()
