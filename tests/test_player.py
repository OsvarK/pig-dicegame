import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
    def test_addScore(self):
        """ Tests Player:addScore"""
        p = Player(None)
        self.assertEqual(p.addScore(100), 100)
        self.assertEqual(p.addScore(100), 200)
        self.assertEqual(p.addScore(100), 300)

    def test_getScore(self):
        """ Tests Player:getScore"""
        p = Player(None)
        self.assertEqual(p.getScore(), 0)
        p.addScore(100)
        self.assertEqual(p.getScore(), 100)


# Run unitest, can also be runnned by 'py -m unititest test_player.py'
if __name__ == '__main__':
    unittest.main()
