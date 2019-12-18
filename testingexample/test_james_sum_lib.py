import unittest

from james_sum_lib import sum_array

class TestSumArray(unittest.TestCase):

    def test_sum_array(self):
        self.assertEqual(sum_array([1, 2, 3]), 6, "Should be 6")



    def test_sum_array_table(self):
        test_cases = [
            {
                "name": "Sum 1 2 3",
                "input": [1, 2, 3],
                "expected": 6
            },
            {
                "name": "Sum Negative Numbers",
                "input": [-1, -2, -3],
                "expected": -6
            },
            {
                "name": "list with one item",
                "input": [100],
                "expected": 100
            },
            {
                "name": "empty list",
                "input": [],
                "expected": 0
            }
        ]
        for test_case in test_cases:
            self.assertEqual(sum_array(test_case["input"]), test_case["expected"], test_case["name"])


if __name__ == '__main__':
    unittest.main()
