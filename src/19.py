with open("./data/input_19_ex.txt") as f:
    patterns = [x.strip() for x in f.readline().strip().split(',')]
    f.readline()
    designs = [l.strip() for l in f]

patterns.sort()
designs.sort()


def match_design(ptns, d, m):
    if d == m:
        return True
    for p in ptns:
        tst = m + p
        if len(tst) <= len(d) and d.startswith(tst) and match_design(ptns, d, tst):
            return True
    return False


print(sum(1 for design in designs if match_design(patterns, design, '')))


def matches(ptns, d, m, acc_m, acc):
    if d == m and acc_m not in acc:
        acc.append(acc_m)
        if len(acc) % 1000 == 0:
            print(len(acc))
    for p in ptns:
        tst = m + p
        if len(tst) <= len(d) and d.startswith(tst):
            acc_m = acc_m.copy()
            acc_m.append(p)
            matches(ptns, d, tst, acc_m, acc)
            acc_m.pop()
    return acc


part2 = 0
for design in designs:
    mat = matches(patterns, design, '', [], [])
    part2 += len(mat)
    # print(design, len(mat))
print(part2)
