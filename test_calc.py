import unittest
import calc

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(4, 5), 9)

    def test_sub(self):
        self.assertEqual(calc.sub(4,2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2,8), 16)

    def test_div(self):
        self.assertEqual(calc.div(8,4), 2)