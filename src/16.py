import numpy as np
import networkx as netx
import matplotlib.pyplot as plt

with open("./data/input_16.txt") as f:
    maze: np.ndarray = np.array([list(line.strip()) for line in f])

st = list(zip(*np.where(maze == 'S')))[0]  # type: ignore
ed = list(zip(*np.where(maze == 'E')))[0]  # type: ignore
maze[st] = '.'
maze[ed] = '.'

# start is east west
st = (st[0], st[1], 'E-W')
ed_ns = (ed[0], ed[1], 'N-S')
ed_ew = (ed[0], ed[1], 'E-W')

ROWS, COLS = maze.shape
G = netx.DiGraph()
for x in range(ROWS):
    for y in range(COLS):
        if maze[x, y] != '.':
            continue
        # north/south plane
        for n_x, n_y, plane in [(x - 1, y, 'N-S'), (x + 1, y, 'N-S'), (x, y + 1, 'E-W'), (x, y - 1, 'E-W')]:
            if 0 <= n_x < ROWS and 0 <= n_y < COLS and maze[n_x, n_y] == '.':
                if plane == 'N-S':
                    G.add_edge((x, y, plane), (n_x, n_y, plane), weight=1)  # N-S plane weight 1
                else:
                    G.add_edge((x, y, 'N-S'), (n_x, n_y, 'E-W'), weight=1001)  # turn node from N-S to east-west
        # east/west plane
        for n_x, n_y, plane in [(x - 1, y, 'N-S'), (x + 1, y, 'N-S'), (x, y + 1, 'E-W'), (x, y - 1, 'E-W')]:
            if 0 <= n_x < ROWS and 0 <= n_y < COLS and maze[n_x, n_y] == '.':
                if plane == 'E-W':
                    G.add_edge((x, y, plane), (n_x, n_y, plane), weight=1)  # E-W plane weight 1
                else:
                    G.add_edge((x, y, 'E-W'), (n_x, n_y, 'N-S'), weight=1001)  # turn node from E-W to north-south


# part 1
cost_ns = netx.dijkstra_path_length(G, source=st, target=ed_ns, weight='weight')
cost_ew = netx.dijkstra_path_length(G, source=st, target=ed_ew, weight='weight')
ed = ed_ns
cost = cost_ns
if cost_ew < cost_ns:
    ed = ed_ew
    cost = cost_ew
path = netx.dijkstra_path(G, source=st, target=ed, weight='weight')
print(cost)

# part 2
visited = {}
all_paths = list(netx.all_shortest_paths(G, source=st, target=ed, weight='weight'))
for path in all_paths:
    for x, y, plane in path:
        visited[x, y] = True
print(len(visited.keys()))

# visualise
G_flat = netx.Graph()
for (x, y, _), (nx, ny, _) in G.edges:
    G_flat.add_edge((x, y), (nx, ny))
normalized_path = [(x, y) for x, y, _ in path]

pos = {node: (node[1], -node[0]) for node in G_flat.nodes}  # For a more conventional plot
plt.figure(figsize=(8, 6))
netx.draw(G_flat, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold')
edges = [(normalized_path[i], normalized_path[i+1]) for i in range(len(normalized_path)-1)]
netx.draw_networkx_edges(G_flat, pos, edgelist=edges, edge_color='red', width=2)
plt.show()
