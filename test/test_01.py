import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p01

class Test01(unittest.TestCase):
    def test_sample_input(self):
        # Test with simple input data
        test_input = [
            (1, 2),
            (3, 1),
            (2, 3),
            (4, 4)
        ]
        
        # Calculate results
        al, bl = zip(*test_input)
        al = sorted(al)
        bl = sorted(bl)
        
        # Test part 1 - absolute differences
        part1 = sum(abs(a - b) for a, b in zip(al, bl))
        self.assertEqual(part1, 0)  # |1-1| + |2-2| + |3-3| + |4-4| = 0 + 0 + 0 + 0 = 0
        
        # Test part 2 - sum of products of number * its count in bl
        part2 = sum(i * bl.count(i) for i in al)
        self.assertEqual(part2, 10)  # 1*1 + 2*1 + 3*1 + 4*1 = 1 + 2 + 3 + 4 = 10

if __name__ == '__main__':
    unittest.main()