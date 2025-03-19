import networkx as netx
from collections import defaultdict
from typing import DefaultDict, List

with open("./data/input_05.txt") as f:  # Restored to use main input
    lines = [line.strip() for line in f]

rules: DefaultDict[int, List[int]] = defaultdict(list)
updates = []
for line in lines:
    if '|' in line:
        p1, p2 = map(int, line.split('|'))
        rules[p1].append(p2)
    elif line:
        updates.append(list(map(int, line.split(','))))


def is_correct_order(update: List[int], rule_dict: defaultdict) -> bool:
    return all(all(p in rule_dict[page] for p in update[idx + 1:]) for idx, page in enumerate(update[:-1]))


correct = [u for u in updates if is_correct_order(u, rules)]
incorrect = [u for u in updates if not is_correct_order(u, rules)]

# part 1
print(sum(update[(len(update) // 2)] for update in correct))

# part 2
part2 = 0
for u in incorrect:
    g = netx.DiGraph()
    g.add_nodes_from(u)
    g.add_edges_from((node, edge) for node in u for edge in rules[node] if edge in u)
    ordered = list(netx.topological_sort(g))
    part2 += ordered[len(ordered) // 2]
print(part2)
