import numpy as np

with open("./data/input_02.txt") as f:
    lines = [list(map(int, l.split())) for l in f]


def is_safe(l):
    diff = np.diff(l)
    return (np.all(diff >= 0) or np.all(diff <= 0)) and np.min(np.abs(diff)) >= 1 and np.max(np.abs(diff)) <= 3


print(sum(is_safe(l) for l in lines))

part2 = sum(
    1 for l in lines
    if is_safe(l) or any(is_safe(l[:i] + l[i + 1:]) for i in range(len(l)))
)
print(part2)
