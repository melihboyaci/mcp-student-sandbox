import unittest

from failing_calculator import average_ratios


class AverageRatiosTests(unittest.TestCase):
    def test_ignores_zero_values_in_average(self):
        self.assertEqual(average_ratios([10, 5, 0]), 15)

    def test_raises_when_all_values_are_zero(self):
        with self.assertRaises(ValueError):
            average_ratios([0, 0, 0])


if __name__ == "__main__":
    unittest.main()
