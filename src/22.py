from collections import defaultdict
from typing import DefaultDict

with open("./data/input_22.txt") as f:
    secrets = [int(l.strip()) for l in f]

NUM_SECRETS = 2000


def mix(n: int, s: int) -> int:
    return n ^ s


def prune(s: int) -> int:
    return s % 16777216


def next_secret(s) -> int:
    s = prune(mix(s * 64, s))
    s = prune(mix(s // 32, s))
    return prune(mix(s * 2048, s))


def secret_chain(s: int, length: int) -> list[int]:
    return [s] + [s := next_secret(s) for _ in range(length)]


def subsequence_index(l: list, s: list) -> int:
    return next((i for i in range(len(l) - len(s) + 1) if l[i:i + len(s)] == s), -1)


# part 1
print(sum(secret_chain(secret, NUM_SECRETS)[-1] for secret in secrets))


# part2
s_dict: DefaultDict[int, list] = defaultdict(list)
for secret in secrets:
    s_dict[secret] = secret_chain(secret, NUM_SECRETS)

all_seq_dict: DefaultDict[tuple, int] = defaultdict(int)
for secret, seq in s_dict.items():
    seq_dict: dict[tuple, int] = {}
    right_most = [abs(x) % 10 for x in seq]
    diffs = [j - i for i, j in zip(right_most[:-1], right_most[1:])]

    for i in range(len(diffs) - 4 + 1):
        code = tuple(diffs[i:i + 4])
        val = right_most[i+4]
        if code not in seq_dict:
            seq_dict[code] = val
    for code, val in seq_dict.items():
        all_seq_dict[code] += val

print(max(all_seq_dict.values()))
