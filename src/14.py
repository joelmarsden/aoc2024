import numpy as np
from collections import defaultdict
import re

with open("./data/input_14.txt") as f:
    lines = [line.strip().split(' ') for line in f]
    robots = [(tuple(map(int, (p.split('=')[1].split(',')))), (tuple(map(int, (v.split('=')[1].split(',')))))) for p, v
              in lines]

WIDTH, HEIGHT = 101, 103
MID_W, MID_H = WIDTH // 2, HEIGHT // 2
STEPS = 100


def move_robots(r: list, steps: int) -> list:
    final_locations = []
    for p, v in r:
        x = (p[0] + steps * v[0]) % WIDTH
        y = (p[1] + steps * v[1]) % HEIGHT
        final_locations.append((x, y))
    return final_locations


def count_by_quadrant(r: list) -> dict:
    quadrants = defaultdict(int)
    for x, y in r:
        q = 0
        if x < MID_W and y < MID_H:
            q = 1
        elif x > MID_W and y < MID_H:
            q = 2
        elif x < MID_W and y > MID_H:
            q = 3
        elif x > MID_W and y > MID_H:
            q = 4
        if q > 0:
            quadrants[q] += 1  # type: ignore
    return quadrants


def to_matrix(r: list):
    grid = np.full((WIDTH, HEIGHT), ' ')
    for x, y in r:
        grid[x, y] = '#'  # type: ignore
    return grid


print(np.prod(list(count_by_quadrant(move_robots(robots, STEPS)).values())))

PATTERN = "#" * 15
for stps in range(50000):
    grd = to_matrix(move_robots(robots, stps))
    if sum(1 for row in grd if re.search(PATTERN, ''.join(row))) >= 2:  # type: ignore
        print(f'candidate: {stps}')
        np.savetxt(f'../out/aoc_14_{stps}.txt', grd, fmt="%s", delimiter="")  # type: ignore
