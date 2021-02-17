import unittest
import math


# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


class TestMath(unittest.TestCase):      # <- inheritate from unittest
    def test_add(self):                 # test_ to know its a test function
        result = math.add(10, 5)        # the math.add(10 + 5) shulde return 15
        self.assertEqual(result, 15)    # check if the result is 15


# Run unitest, can also be runnned by 'py -m unititest test_math.py'
if __name__ == '__main__':
    unittest.main()
