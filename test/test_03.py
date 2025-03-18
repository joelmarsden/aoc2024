import unittest
import re
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p03

class Test03(unittest.TestCase):
    def test_multiplication(self):
        # Test basic multiplication pattern
        self.assertEqual(p03.mul("mul(2,3)"), 6)
        self.assertEqual(p03.mul("mul(4,5)mul(2,2)"), 24)  # 20 + 4
        
        # Test multiple multiplications
        self.assertEqual(p03.mul("something mul(3,3) text mul(2,4)"), 17)  # 9 + 8
        
    def test_with_do_operations(self):
        # Test sample case with do() operations
        line = "do()mul(2,3)mul(3,4)don't()mul(5,5)"
        idxes = {}
        for idx in re.finditer(r'do\(\)', line):
            idxes[idx.end()] = True
        for idx in re.finditer(r"don't\(\)", line):
            idxes[idx.end()] = False
        idxes = {k: idxes[k] for k in sorted(idxes)}
        
        lastIdx, last = 0, True
        result = 0
        for idx, val in idxes.items():
            if last is True:
                result += p03.mul(line[lastIdx:idx])
            lastIdx, last = idx, val
        if last is True:
            result += p03.mul(line[lastIdx:])
            
        self.assertEqual(result, 18)  # mul(2,3) + mul(3,4) = 6 + 12 = 18

if __name__ == '__main__':
    unittest.main()