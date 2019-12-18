import unittest

from day1 import calcFuelPerUnitMass


class TestFuelCalc(unittest.TestCase):

    def test_calcFuel(self):
        test_cases = [
            {
                "name": "Fuel for Mass 12",
                "input": 12,
                "expected": 2
            },
            {
                "name": "Fuel for Mass 14",
                "input": 14,
                "expected": 2
            },
            {
                "name": "Fuel for Mass 1969",
                "input": 1969,
                "expected": 654
            },
            {
                "name": "Fuel for Mass 100756",
                "input": 100756,
                "expected": 33583
            },
        ]
        for test_case in test_cases:
            self.assertEqual(
                calcFuel(test_case["input"]), test_case["expected"], test_case["name"])


if __name__ == '__main__':
    unittest.main()
