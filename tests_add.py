import unittest
from test import MyCalculator


class TestAddNumbers(unittest.TestCase):

    def setUp(self):
        self.calculator = MyCalculator()

    def test_add_two_numbers(self):

        self.assertEqual(5, self.calculator.add("2, 3"))
        self.assertNotEqual(4, self.calculator.add("2,3"))
