import numpy as np
import networkx as netx

with open("./data/input_18.txt") as f:
    byte_list = [tuple(map(int, l.strip().split(','))) for l in f]

WIDTH, HEIGHT = 71, 71
STEPS = 1024


def build_graph(m: np.ndarray) -> netx.DiGraph:
    rows, cols = m.shape
    g = netx.DiGraph()
    for i in range(rows):
        for j in range(cols):
            if m[i, j] == '#':
                continue
            for nx, ny in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nx < rows and 0 <= ny < cols and m[nx, ny] == '.':
                    g.add_edge((i, j), (nx, ny))
    return g


# part 1
mem_space: np.ndarray = np.full((WIDTH, HEIGHT), '.')
for x, y in byte_list[:STEPS]:
    mem_space[y, x] = '#'

graph = build_graph(mem_space)
print(netx.dijkstra_path_length(graph, source=(0, 0), target=(WIDTH-1, HEIGHT-1), weight='weight'))

# part 2
mem_space: np.ndarray = np.full((WIDTH, HEIGHT), '.')
for idx, (x, y) in enumerate(byte_list):
    mem_space[y, x] = '#'
    if idx >= STEPS:
        graph = build_graph(mem_space)
        if not netx.has_path(graph, source=(0, 0), target=(WIDTH-1, HEIGHT-1)):
            print(f'No path found at index {idx}: ({x},{y})')
            break
