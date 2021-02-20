import unittest
from pigdicegame.userInterface import UserInterface
from pigdicegame.player import Player


class TestUserInterface(unittest.TestCase):

    def throwDiceLoop(self):
        """ Tests UserInterface:throwDiceLoop"""
        ui = UserInterface()
        player = Player()
        result = ui.throwDiceLoop(player)
        self.assertTrue(result in range(-1, 6))


# Run by typing: py <filename>
if __name__ == '__main__':
    unittest.main()
