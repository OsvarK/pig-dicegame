import unittest
import calc

# https://www.youtube.com/watch?v=6tNS--WetLI   <-- video for this example!

# Diffrent pre made assert fucntions can found here!
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


class TestMath(unittest.TestCase):  # <- inheritate from unittest

    # test_ to know its a test function
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # try an exception error
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# Dont do many tests, do smart tests.

# Run unitest, can also be runnned by 'py -m unititest test_math.py'
if __name__ == '__main__':
    unittest.main()

# Coverage --------------------------------------------------------------------
# to check coverage, type 'coverage run <test_file.py>'
# get html report: 'coverage html'
# get report: 'coverage report'
