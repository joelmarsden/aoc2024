import networkx as nx

with open("./data/input_23_ex.txt") as f:
    connections = [tuple(l.strip().split('-')) for l in f]

graph = nx.Graph(connections)  # type: ignore

# part 1
triangles = [list(t) for t in nx.enumerate_all_cliques(graph) if len(t) == 3]
print(sum(1 for t in triangles if any(x.startswith('t') for x in t)))

# part 2
largest = max(nx.find_cliques(graph), key=len)
print(','.join(map(str, sorted(largest))))
