import unittest
import networkx as netx
from collections import defaultdict
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import p05

class Test05(unittest.TestCase):
    def setUp(self):
        # Example rules from input_05_ex.txt
        self.test_rules = defaultdict(list)
        # Sample rule definitions
        rule_data = [
            (47, 53), (97, 13), (97, 61), (97, 47),
            (75, 29), (61, 13), (75, 53), (29, 13),
            (97, 29), (53, 29), (61, 53), (97, 53),
            (61, 29), (47, 13), (75, 47), (97, 75),
            (47, 61), (75, 61), (47, 29), (75, 13),
            (53, 13)
        ]
        for p1, p2 in rule_data:
            self.test_rules[p1].append(p2)

        # Sample test cases from example input
        self.test_updates = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47]
        ]

    def test_rule_parsing(self):
        # Test that rules are properly parsed
        self.assertTrue(13 in self.test_rules[97])
        self.assertTrue(53 in self.test_rules[47])
        self.assertEqual(len(self.test_rules[75]), 5)  # 75 should have 5 dependencies

    def test_correct_order(self):
        # Test the is_correct_order function with known examples
        correct_updates = [u for u in self.test_updates if p05.is_correct_order(u, self.test_rules)]
        incorrect_updates = [u for u in self.test_updates if not p05.is_correct_order(u, self.test_rules)]
        
        # Test specific cases from example input
        self.assertTrue(p05.is_correct_order([75, 47, 61, 53, 29], self.test_rules))
        self.assertFalse(p05.is_correct_order([75, 97, 47, 61, 53], self.test_rules))
        self.assertEqual(len(correct_updates), 3)  # Should have 3 correct sequences
        self.assertEqual(len(incorrect_updates), 3)  # Should have 3 incorrect sequences

    def test_part1_calculation(self):
        correct = [u for u in self.test_updates if p05.is_correct_order(u, self.test_rules)]
        result = sum(update[len(update) // 2] for update in correct)
        self.assertEqual(result, 143)  # Verify the middle element sum for correct sequences

    def test_part2_calculation(self):
        incorrect = [u for u in self.test_updates if not p05.is_correct_order(u, self.test_rules)]
        part2 = 0
        for u in incorrect:
            g = netx.DiGraph()
            g.add_nodes_from(u)
            g.add_edges_from((node, edge) for node in u for edge in self.test_rules[node] if edge in u)
            ordered = list(netx.topological_sort(g))
            part2 += ordered[len(ordered) // 2]
        self.assertEqual(part2, 123)  # Updated to correct value from example input

if __name__ == '__main__':
    unittest.main()