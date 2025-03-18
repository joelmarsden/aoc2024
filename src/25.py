import numpy as np

with open("./data/input_25.txt") as f:
    locks, keys, l = [], [], []
    for line in f:
        line = line.strip()
        if not line:
            if l:
                (locks if l[0][0] == '#' else keys).append(np.array(l))
            l = []
        else:
            l.append(list(line))
    if l:
        (locks if l[0][0] == '#' else keys).append(np.array(l))


def count_pins(diagrams, is_key=False):
    pins = []
    for d in diagrams:
        pin = []
        for col in range(d.shape[1]):
            s = ''.join(d[1:, col])
            if is_key:
                s = s[:-1][::-1]
            cnt = sum(1 for c in s if c == '#' and ('.' not in s or s.index(c) < s.index('.')))
            pin.append(cnt)
        pins.append(pin)
    return pins


def fits(lock, key):
    return all(a + b <= 5 for a, b in zip(lock, key))


lock_pins = count_pins(locks)
key_pins = count_pins(keys, is_key=True)
print(sum(1 for lock in lock_pins for key in key_pins if fits(lock, key)))
