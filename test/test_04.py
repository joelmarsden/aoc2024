import unittest
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p04

class Test04(unittest.TestCase):
    def setUp(self):
        # Example input matrix
        self.test_matrix = np.array([
            list("MMMSXXMASM"),
            list("MSAMXMSMSA"),
            list("AMXSXMAAMM"),
            list("MSAMASMSMX"),
            list("XMASAMXAMM"),
            list("XXAMMXXAMA"),
            list("SMSMSASXSS"),
            list("SAXAMASAAA"),
            list("MAMMMXMMMM"),
            list("MXMXAXMASX")
        ])

    def test_xmas_count(self):
        # Test counting XMAS in a string and its reverse
        self.assertEqual(p04.xmas_count("XMAS"), 1)
        self.assertEqual(p04.xmas_count("SAMX"), 1)  # Reversed XMAS
        self.assertEqual(p04.xmas_count("XMASSAMX"), 2)  # One forward, one reverse
        self.assertEqual(p04.xmas_count("AMSX"), 0)  # No XMAS pattern

    def test_get_diagonals(self):
        # Test with a smaller matrix to verify diagonal extraction
        small_matrix = np.array([
            ['X', 'M', 'A'],
            ['M', 'A', 'S'],
            ['A', 'S', 'X']
        ])
        diagonals = p04.get_diagonals(small_matrix)
        
        # Should contain both main diagonals and all sub-diagonals
        expected_diagonals = [
            ['A'], ['M', 'S'], ['X', 'A', 'X'],  # Top-left to bottom-right
            ['M'], ['A'], 
            ['A'], ['M', 'S'], ['X', 'A', 'X'],  # Top-right to bottom-left (flipped)
            ['M'], ['A']
        ]
        
        # Convert numpy arrays to lists for comparison
        actual_diagonals = [d for d in diagonals]
        self.assertEqual(len(actual_diagonals), len(expected_diagonals))
        
        # Check that all expected diagonals are present
        for exp_diag in expected_diagonals:
            self.assertTrue(any(all(a == b for a, b in zip(exp_diag, act_diag)) 
                              for act_diag in actual_diagonals))

    def test_part1_example(self):
        # Test part 1 with the example input
        part1 = sum(p04.xmas_count(''.join(line)) for lines in 
                   [self.test_matrix, self.test_matrix.T, p04.get_diagonals(self.test_matrix)] 
                   for line in lines)
        self.assertEqual(part1, 18)  # Based on example input result

    def test_part2_example(self):
        # Test part 2 with the example input
        part2 = 0
        rows, cols = self.test_matrix.shape
        for r in range(rows-2):
            for c in range(cols-2):
                s1 = ''.join(self.test_matrix[r, c] + self.test_matrix[r + 1, c + 1] + 
                           self.test_matrix[r + 2, c + 2])
                s2 = ''.join(self.test_matrix[r + 2, c] + self.test_matrix[r + 1, c + 1] + 
                           self.test_matrix[r, c + 2])
                if (s1 == 'MAS' or s1[::-1] == 'MAS') and (s2 == 'MAS' or s2[::-1] == 'MAS'):
                    part2 += 1
        self.assertEqual(part2, 9)  # Based on example input result

if __name__ == '__main__':
    unittest.main()