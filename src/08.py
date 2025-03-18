import numpy as np
import itertools


with open("./data/input_08.txt") as f:
    maze: np.ndarray = np.array([list(line.strip()) for line in f])


def is_inbound(m: np.ndarray, x, y):
    return 0 <= x < m.shape[0] and 0 <= y < m.shape[1]


def antinode_count(m: np.ndarray, repeat: bool):
    antinodes = {}    # type: ignore
    unique_chars = np.unique(m)
    unique_chars = unique_chars[unique_chars != '.']
    for c in unique_chars:    # type: ignore
        for (x1, y1), (x2, y2) in (itertools.combinations(np.argwhere(m == c), 2)):
            if repeat:
                antinodes[(x1, y1)] = True
                antinodes[(x2, y2)] = True
            xd, yd = abs(x1 - x2), abs(y1 - y2)
            n = 1
            while True:
                xn1 = (x1 - n*xd) if x1 <= x2 else (x1 + n*xd)
                yn1 = (y1 - n*yd) if y1 <= y2 else (y1 + n*yd)
                if is_inbound(m, xn1, yn1):
                    antinodes[(xn1, yn1)] = True
                else:
                    break
                if not repeat:
                    break
                n += 1
            n = 1
            while True:
                xn2 = (x2 + n*xd) if x2 > x1 else (x2 - n*xd)
                yn2 = (y2 + n*yd) if y2 > y1 else (y2 - n*yd)
                if is_inbound(m, xn2, yn2):
                    antinodes[(xn2, yn2)] = True
                else:
                    break
                if not repeat:
                    break
                n += 1
    return len(antinodes)


print(antinode_count(maze, False))
print(antinode_count(maze, True))
