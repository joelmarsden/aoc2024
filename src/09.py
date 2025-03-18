from collections import deque

with open("./data/input_09.txt") as f:
    diskmap = list(map(int, f.readline().strip()))

# part 1
disk_q: deque = deque()
for pos, digit in enumerate(diskmap):
    if pos % 2 == 0:
        idx = pos // 2
        disk_q.extend([idx] * digit)
    else:
        disk_q.extend([-1] * digit)

disk_out = []
while disk_q:
    i = disk_q.popleft()
    if not i == -1:
        disk_out.append(i)
    else:
        while disk_q and disk_q[-1] == -1:
            disk_q.pop()
        if disk_q:
            disk_out.append(disk_q.pop())

checksum = sum(idx * c for idx, c in enumerate(disk_out))
print(checksum)


def find_first_free_idx(q, size):
    for i_dx, (blk, _, sz) in enumerate(q):
        if blk == 'D':
            continue
        if sz >= size:
            return i_dx
    return -1


def to_str(q):
    return ''.join(str(id_x) * count if blk == 'D' else '.' * count for (blk, id_x, count) in q)


def to_arr(q):
    return [id_x if blk == 'D' else -1 for blk, id_x, count in q for _ in range(count)]


# part 2
disk_q: []
for pos, digit in enumerate(diskmap):
    if pos % 2 == 0:
        idx = pos // 2
        disk_q.append(('D', idx, digit))
    else:
        if digit > 0:
            disk_q.append(('F', 0, digit))

for block, idx, cnt in reversed(disk_q.copy()):
    if block == 'F':
        continue
    free_idx = find_first_free_idx(disk_q, cnt)
    cur_idx = disk_q.index((block, idx, cnt))
    if free_idx != -1 and free_idx < cur_idx:
        # move the block to free space
        move_idx = disk_q.index((block, idx, cnt))
        disk_q.remove((block, idx, cnt))
        disk_q.insert(move_idx, ('F', 0, cnt))  # becomes free space
        disk_q.insert(free_idx, (block, idx, cnt))
        # update free cnt of the block we moved to
        fb, fi, fc = disk_q[free_idx+1]
        disk_q.remove((fb, fi, fc))
        fc -= cnt
        if fc > 0:
            disk_q.insert(free_idx+1, (fb, fi, fc))
        # compact the free space
        dq_2 = []
        fc = 0
        for x in disk_q:
            if x[0] == 'D':
                if fc > 0:
                    dq_2.append(('F', 0, fc))
                    fc = 0
                dq_2.append(x)
            else:
                fc += x[2]
        disk_q = dq_2  # type: ignore


checksum = sum(i * num for i, num in enumerate(to_arr(disk_q)) if num >= 0)
print(checksum)
