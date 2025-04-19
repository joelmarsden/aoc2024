import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p07

class Test07(unittest.TestCase):
    def setUp(self):
        # Load example data from input_07_ex.txt
        self.test_data = p07.load_data("input_07_ex.txt")

    def test_load_data(self):
        # Test that data is loaded correctly
        self.assertEqual(len(self.test_data), 9)  # 9 lines in example file

        # Check first entry
        self.assertEqual(self.test_data[0][0], 190)  # Total is 190
        self.assertEqual(self.test_data[0][1], [10, 19])  # Numbers are [10, 19]

        # Check another entry
        self.assertEqual(self.test_data[4][0], 7290)  # Total is 7290
        self.assertEqual(self.test_data[4][1], [6, 8, 6, 15])  # Numbers are [6, 8, 6, 15]

    def test_find_eqn_basic_operators(self):
        # Test with only + and * operators

        # 190: 10 19 (10 * 19 = 190)
        self.assertTrue(p07.find_eqn(190, [10, 19], ['+', '*']))

        # 83: 17 5 (17 + 5 = 22, not 83)
        self.assertFalse(p07.find_eqn(83, [17, 5], ['+', '*']))

        # 156: 15 6 (15 + 6 = 21, 15 * 6 = 90, neither is 156)
        self.assertFalse(p07.find_eqn(156, [15, 6], ['+', '*']))

        # 7290: 6 8 6 15 (6 * 8 * 6 * 15 = 4320, not 7290)
        self.assertFalse(p07.find_eqn(7290, [6, 8, 6, 15], ['+', '*']))

    def test_find_eqn_with_concatenation(self):
        # Test with +, *, and || operators

        # 83: 17 5 (17 || 5 = 175, not 83)
        self.assertFalse(p07.find_eqn(83, [17, 5], ['+', '*', '||']))

        # 156: 15 6 (15 || 6 = 156)
        self.assertTrue(p07.find_eqn(156, [15, 6], ['+', '*', '||']))

        # 161011: 16 10 13 (16 || 10 || 13 = 161013, not 161011)
        self.assertFalse(p07.find_eqn(161011, [16, 10, 13], ['+', '*', '||']))

    def test_part1(self):
        # Test part1 function with example data
        # The sum of all valid equations with + and * operators
        result = p07.part1(self.test_data)
        self.assertEqual(result, 3749)

    def test_part2(self):
        # Test part2 function with example data
        # The sum of all valid equations with +, *, and || operators
        result = p07.part2(self.test_data)
        self.assertEqual(result, 11387)

if __name__ == '__main__':
    unittest.main()
