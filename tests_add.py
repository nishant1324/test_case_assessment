import unittest
from test import MyCalculator


class TestAddNumbers(unittest.TestCase):

    def setUp(self):
        self.calculator = MyCalculator()

    def test_add_two_numbers(self):

        self.assertEqual(5, self.calculator.add("2, 3"))
        self.assertNotEqual(4, self.calculator.add("2,3"))

    def test_add_one_numbers(self):

        self.assertEqual(2, self.calculator.add("2"))

    def test_add_zero_numbers(self):

        self.assertEqual(0, self.calculator.add(""))

    def test_add_multiple_numbers(self):

        self.assertEqual(17, self.calculator.add("2, 3, 4, 8"))

    def test_add_negative_numbers(self):
        with self.assertRaises(ValueError) as error:
            self.calculator.add("-1,-2,3")
            self.assertEqual(
                str(error.exception), "negative numbers not allowed: -1, -2"
            )

    def test_delimiter_in_number_addition(self):
        self.assertEqual(8, self.calculator.add("1\n2,5"))

    def test__different_delimiter(self):
        self.assertEqual(8, self.calculator.add("//;\n1;7"))

    def test_escaped_delimiter(self):
        with self.assertRaises(ValueError) as error:
            self.assertEqual(self.calculator.add("1\\,2\\,3"), 6)

    def test_ignore_numbers_greaterthan_1000(self):
        self.assertEqual(self.calculator.add("1000 ,2000"), 1000)
