import numpy as np
import networkx as netx

with open("./data/input_20.txt") as f:
    maze: np.ndarray = np.array([list(line.strip()) for line in f])

st = list(zip(*np.where(maze == 'S')))[0]  # type: ignore
ed = list(zip(*np.where(maze == 'E')))[0]  # type: ignore
maze[st] = '.'
maze[ed] = '.'

MIN_SAVING = 100


def build_graph(m: np.ndarray, wall) -> netx.DiGraph:
    rows, cols = m.shape
    g = netx.DiGraph()
    for i in range(rows):
        for j in range(cols):
            if m[i, j] == '#' and m[i, j] != wall:
                continue
            for nx, ny in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nx < rows and 0 <= ny < cols and m[nx, ny] == '.':
                    g.add_edge((i, j), (nx, ny))
    return g


base_cost = netx.dijkstra_path_length(build_graph(maze, (0, 0)), source=st, target=ed, weight='weight')
print(base_cost)


ROWS, COLS = maze.shape
part1 = 0
for x in range(1, ROWS - 1):
    for y in range(1, COLS - 1):
        if maze[x, y] == '#':
            maze[x, y] = '.'
            graph = build_graph(maze, (x, y))
            path_len = netx.dijkstra_path_length(graph, source=st, target=ed, weight='weight')
            maze[x, y] = '#'
            if base_cost - path_len >= MIN_SAVING:
                print(f'{x},{y}: {path_len}')
                part1 += 1
print(part1)
