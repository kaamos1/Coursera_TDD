import unittest
from compute_stats_refactor import *


class TestComputeStats(unittest.TestCase):
    def test_harmonic_mean(self):
        test_data = [1, 4, 4]
        self.assertEqual(harmonic_mean(test_data), 2)

    def test_harmonic_mean_no_values(self):
        test_data = []
        try:
            result = harmonic_mean(test_data)
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        else:
            self.fail("Did not raise exception")

    def test_variance(self):
        test_data = [1, 2, 3]
        self.assertEqual(variance(test_data), 1)

    def test_standard_dev(self):
        test_data = [1, 2, 3]
        self.assertEqual(standard_dev(test_data), 1)


if __name__ == '__main__':
    unittest.main()
