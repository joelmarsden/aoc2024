with open("./data/input_11.txt") as f:
    st = list(map(int, f.readline().strip().split()))


def blink(stones):
    t = []
    for s in stones:
        if s == 0:
            t.append(1)
        elif len(str(s)) % 2 == 0:
            mid = len(str(s)) // 2
            t.extend([int(str(s)[:mid]), int(str(s)[mid:])])
        else:
            t.append(s*2024)
    return t


for idx in range(25):
    st = blink(st)
print(len(st))
