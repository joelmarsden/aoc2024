import re
import math

with open("./data/input_03.txt") as f:
    lines = [''.join(line.strip() for line in f)]


def mul(s):
    return sum(math.prod(map(int, match)) for match in re.findall(r'mul\((\d+),(\d+)\)', s))


print(sum(mul(l) for l in lines))

part2 = 0
for l in lines:
    idxes = {}
    for idx in re.finditer(r'do\(\)', l):
        idxes[idx.end()] = True
    for idx in re.finditer(r"don't\(\)", l):
        idxes[idx.end()] = False
    idxes = {k: idxes[k] for k in sorted(idxes)}

    lastIdx, last = 0, True
    for idx, val in idxes.items():
        if last is True:
            part2 += mul(l[lastIdx:idx])
        lastIdx, last = idx, val
    if last is True:
        part2 += mul(l[lastIdx:])
print(part2)
