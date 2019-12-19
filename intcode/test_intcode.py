import unittest

from intcode import intcode



class TestIntCodeMemoryResult(unittest.TestCase):

    def test_intcode(self):
        test_cases = [
            {
                "name": "1,0,0,0,99 (1 + 1 = 2)",
                "input": "1,0,0,0,99",
                "expected": [2, 0, 0, 0, 99]
            },
            {
                "name": "2,3,0,3,99 (3 * 2 = 6)",
                "input": "2,3,0,3,99",
                "expected": [2, 3, 0, 6, 99]
            },
            {
                "name": "2,4,4,5,99,0 (99 * 99 = 9801)",
                "input": "2,4,4,5,99,0",
                "expected": [2, 4, 4, 5, 99, 9801]
            },
            {
                "name": "1,1,1,4,99,5,6,0,99 -> 30,1,1,4,2,5,6,0,99",
                "input": "1,1,1,4,99,5,6,0,99",
                "expected": [30, 1, 1, 4, 2, 5, 6, 0, 99]
            },

        ]
        for test_case in test_cases:
            computer = intcode()
            computer.loadProgram(test_case["input"])
            computer.execute()
            self.assertEqual(
               computer.memory, test_case["expected"], test_case["name"])


if __name__ == '__main__':
    unittest.main()
