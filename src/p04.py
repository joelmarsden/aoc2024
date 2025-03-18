import numpy as np
import re

with open("./data/input_04.txt") as f:
    matrix: np.ndarray = np.array([list(line.strip()) for line in f])


def xmas_count(s):
    return len((re.findall(r'XMAS', s))) + len((re.findall(r'XMAS', s[::-1])))


def get_diagonals(m):
    arr: np.ndarray = np.array(m)
    diagonals = []

    # Top-left to bottom-right diagonals
    for offset in range(-arr.shape[0] + 1, arr.shape[1]):
        diagonals.append(arr.diagonal(offset).tolist())

    # Top-right to bottom-left diagonals
    flipped_arr: np.ndarray = np.fliplr(arr)  # Flip the array left-to-right
    for offset in range(-flipped_arr.shape[0] + 1, flipped_arr.shape[1]):
        diagonals.append(flipped_arr.diagonal(offset).tolist())

    return diagonals


part1 = sum(xmas_count(''.join(line)) for lines in [matrix, matrix.T, get_diagonals(matrix)] for line in lines)
print(part1)

# part 2
part2 = 0
rows, cols = matrix.shape
for r in range(rows-2):
    for c in range(cols-2):
        s1 = ''.join(matrix[r, c] + matrix[r + 1, c + 1] + matrix[r + 2, c + 2])
        s2 = ''.join(matrix[r + 2, c] + matrix[r + 1, c + 1] + matrix[r, c + 2])
        if (s1 == 'MAS' or s1[::-1] == 'MAS') and (s2 == 'MAS' or s2[::-1] == 'MAS'):
            part2 += 1
print(part2)
