import unittest
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p06

class Test06(unittest.TestCase):
    def setUp(self):
        # Example maze from input_06_ex.txt
        self.test_maze = np.array([
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
            list("........#."),
            list("#........."),
            list("......#...")
        ])
        
    def test_find_character(self):
        # Test finding start position (^)
        pos = p06.find_character(self.test_maze, '^')
        self.assertEqual(pos, (6, 4))  # ^ is at row 6, col 4
        
        # Test finding a wall (#)
        pos = p06.find_character(self.test_maze, '#')
        self.assertEqual(pos, (0, 4))  # First # is at row 0, col 4
        
        # Test finding non-existent character
        pos = p06.find_character(self.test_maze, '@')
        self.assertIsNone(pos)

    def test_walk_maze(self):
        # Test walking the maze marks correct number of spaces
        result = p06.walk_maze(self.test_maze.copy())
        self.assertEqual(result, 41)  # Sum of X and $ markers in example
        
        # Verify the original maze is unchanged
        self.assertEqual(self.test_maze[6, 4], '^')  # Start position still has ^

    def test_part2_calculation(self):
        # Test part 2 wall placement counting
        part2 = 0
        for row in range(self.test_maze.shape[0]):
            for col in range(self.test_maze.shape[1]):
                if self.test_maze[row, col] == '.':
                    m = self.test_maze.copy()
                    m[row, col] = '#'
                    x = p06.walk_maze(m)
                    if x == 0:
                        part2 += 1
        self.assertEqual(part2, 6)  # Number of possible wall placements that block the path

    def test_maze_boundaries(self):
        # Test maze walking with boundary conditions
        small_maze = np.array([
            list("^..."),
            list("...."),
            list("...."),
            list("...#")
        ])
        result = p06.walk_maze(small_maze.copy())
        self.assertGreater(result, 0)  # Should mark some spaces before hitting boundary

if __name__ == '__main__':
    unittest.main()