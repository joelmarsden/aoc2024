import numpy as np

with open("./data/input_06.txt") as f:
    maze: np.ndarray = np.array([list(line.strip()) for line in f])


def find_character(matrix, char):
    result = np.argwhere(matrix == char)
    return tuple(result[0]) if result.size > 0 else None  # Return the first match or None


def walk_maze(matrix: np.ndarray):
    rows, cols = matrix.shape
    r, c = find_character(matrix, '^')
    dirn = 'N'

    steps = 0
    while True:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            break
        matrix[r, c] = '$' if matrix[r, c] == 'X' else 'X'
        if steps > 10_000:  # this is a hack - should really find_character(m, 'X') is None but has a logic issue
            return 0
        match dirn:
            case 'N':
                if r == 0: break    # noqa: E701
                if matrix[r - 1, c] == '#':
                    dirn = 'E'
                else:
                    r -= 1
            case 'E':
                if c+1 == cols: break  # noqa: E701
                if matrix[r, c + 1] == '#':
                    dirn = 'S'
                else:
                    c += 1
            case 'W':
                if c == 0: break  # noqa: E701
                if matrix[r, c - 1] == '#':
                    dirn = 'N'
                else:
                    c -= 1
            case 'S':
                if r+1 == rows: break  # noqa: E701
                if matrix[r + 1, c] == '#':
                    dirn = 'W'
                else:
                    r += 1
        steps += 1
    return np.sum(matrix == 'X') + np.sum(matrix == '$')


# part 1
print(walk_maze(maze.copy()))

# part 2
part2 = 0
for row in range(maze.shape[0]):
    for col in range(maze.shape[1]):
        if maze[row, col] == '.':
            m = maze.copy()
            m[row, col] = '#'
            x = walk_maze(m)
            if x == 0:
                part2 += 1
print(part2)
