import numpy as np
import networkx as netx

with open("./data/input_10.txt") as f:
    topo: np.ndarray = np.array([list(map(int, line.strip())) for line in f])

from_locs = list(zip(*np.where(topo == 0)))  # type: ignore
to_locs = list(zip(*np.where(topo == 9)))  # type: ignore

ROWS, COLS = topo.shape
G = netx.DiGraph()
for x in range(ROWS):
    for y in range(COLS):
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < ROWS and 0 <= ny < COLS and (topo[nx, ny] - topo[x, y]) == 1:
                G.add_edge((x, y), (nx, ny))

print(sum(1 for st in from_locs for ed in to_locs if netx.has_path(G, source=st, target=ed)))
print(sum(sum(1 for _ in netx.all_simple_paths(G, source=st, target=ed)) for st in from_locs for ed in to_locs))
