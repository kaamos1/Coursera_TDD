import unittest
from tested_functions import adder


class TestAdder(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_numbers_correctly(self):
        self.assertEqual(adder(-1, -4), -5)

    def test_adds_numbers_to_zero_correctly(self):
        self.assertEqual(adder(3, 0), 3)

    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(1, 2, 3), 6)

    def test_adds_forty_integers_correctly(self):
        self.assertEqual(adder(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 40)

    def test_raises_an_exception_when_given_one_argument(self):
        try:
            result = adder(3)
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Did not raise exception")

    def test_raises_an_exception_on_string_arguments(self):
        try:
            result = adder(3, "12")
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        else:
            self.fail("Did not raise exception")


if __name__ == '__main__':
    unittest.main()
