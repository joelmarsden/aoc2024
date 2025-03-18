import unittest
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p02

class Test02(unittest.TestCase):
    def test_sample_sequences(self):
        # Test ascending sequences with valid differences
        self.assertTrue(p02.is_safe([1, 2, 3, 4]))  # diff=1
        self.assertTrue(p02.is_safe([1, 3, 5, 7]))  # diff=2
        
        # Test descending sequences with valid differences
        self.assertTrue(p02.is_safe([7, 5, 3, 1]))  # diff=-2
        self.assertTrue(p02.is_safe([4, 3, 2, 1]))  # diff=-1
        
        # Test invalid sequences
        self.assertFalse(p02.is_safe([1, 4, 7, 11]))  # diff > 3
        self.assertFalse(p02.is_safe([10, 6, 2, -3]))  # diff < -3
        self.assertFalse(p02.is_safe([1, 2, 2, 3]))  # diff = 0 in middle
        self.assertFalse(p02.is_safe([1, 3, 2, 4]))  # not monotonic

    def test_part2_examples(self):
        # Test sequences that become safe after removing one element
        seq = [1, 2, 6, 3]  # Removing 6 makes it safe
        self.assertTrue(
            p02.is_safe(seq) or 
            any(p02.is_safe(seq[:i] + seq[i + 1:]) for i in range(len(seq)))
        )

if __name__ == '__main__':
    unittest.main()