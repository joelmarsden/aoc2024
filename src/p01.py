with open("./data/input_01.txt") as f:
    lines = [tuple(map(int, l.split())) for l in f]

al, bl = zip(*lines)
al = sorted(al)
bl = sorted(bl)

print(sum(abs(a - b) for a, b in zip(al, bl)))
print(sum(i * bl.count(i) for i in al))
