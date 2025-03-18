import numpy as np
import re

with open("./data/input_15.txt") as f:
    reading_maze = True
    maze_input, base_directions = [], []
    for line in f:
        line = line.strip()
        if not line:
            reading_maze = False
            continue
        if reading_maze:
            maze_input.append(line)
        else:
            base_directions.extend(line)
    base_maze: np.ndarray = np.array([list(row) for row in maze_input])


def find_first_dot_or_hash(s):
    res = re.search(r'[.#]', s)
    return (res.group(), res.start()) if res else (None, None)


def process_maze(maze: np.ndarray, directions):

    def process_slice(slice_):
        new_slice = slice_.copy()
        assert(slice_[0] == '@')
        match(new_slice[1]):
            case('#'):
                return new_slice
            case('.'):
                new_slice[:2] = ['.', '@']
                return new_slice
            case('O'):
                fst, idx = find_first_dot_or_hash(''.join(new_slice))
                if fst == '.':
                    new_slice[:2] = ['.', '@']
                    new_slice[idx] = 'O'
                return new_slice
        return new_slice

    r_loc = tuple(np.argwhere(maze == '@')[0])

    for dirn in directions:
        match dirn:
            case '^':
                m_slice = maze[:r_loc[0] + 1, r_loc[1]][::-1]   # reverse for consistent processing
                maze[:r_loc[0] + 1, r_loc[1]] = process_slice(m_slice)[::-1]
                if m_slice[0] == '.':
                    r_loc = (r_loc[0]-1, r_loc[1])
            case 'v':
                m_slice = maze[r_loc[0]:, r_loc[1]]
                maze[r_loc[0]:, r_loc[1]] = process_slice(m_slice)
                if m_slice[0] == '.':
                    r_loc = (r_loc[0]+1, r_loc[1])
            case '<':
                m_slice = maze[r_loc[0], :r_loc[1] + 1][::-1]  # reverse for consistent processing
                maze[r_loc[0], :r_loc[1] + 1] = process_slice(m_slice)[::-1]
                if m_slice[0] == '.':
                    r_loc = (r_loc[0], r_loc[1]-1)
            case '>':
                m_slice = maze[r_loc[0], r_loc[1]:]
                maze[r_loc[0], r_loc[1]:] = process_slice(m_slice)
                if m_slice[0] == '.':
                    r_loc = (r_loc[0], r_loc[1] + 1)
    return maze


def print_maze(maze: np.ndarray):
    for row in maze:
        print(''.join(row))


# part 1
processed_maze = process_maze(base_maze.copy(), base_directions)
print_maze(processed_maze)
print(sum(100 * x + y for x, y in zip(*np.where(processed_maze == 'O'))))  # type: ignore


# part 2
def expand_maze(maze: np.ndarray):
    output_maze = []
    for row in maze:
        output_row = []
        for item in row:
            match item:
                case '#':  output = ['#', '#']
                case 'O':  output = ['[', ']']
                case '.':  output = ['.', '.']
                case '@':  output = ['@', '.']
                case _:    output = ['.', '.']
            output_row.extend(output)
        output_maze.append(output_row)
    return np.array(output_maze)

def process_h_slice(slice_):
    new_slice = slice_.copy()
    assert(slice_[0] == '@')
    match(new_slice[1]):
        case('#'):
            return new_slice
        case('.'):
            new_slice[:2] = ['.', '@']
            return new_slice
        case ('[' | ']'):
            fst, idx = find_first_dot_or_hash(''.join(new_slice))
            if fst == '.':
                # shuffle everything along one until the index
                new_slice = np.insert(np.delete(new_slice, idx), 0, '.')
            return new_slice
    return new_slice


def process_expanded(maze: np.ndarray, directions):

    r_loc = tuple(np.argwhere(maze == '@')[0])

    for dirn in directions:
        match dirn:
            case '^':
                m_slice = maze[:r_loc[0] + 1, r_loc[1]][::-1]   # reverse for consistent processing
                # maze[:r_loc[0] + 1, r_loc[1]] = process_slice(m_slice)[::-1]
                # if m_slice[0] == '.':
                #     r_loc = (r_loc[0]-1, r_loc[1])
            case 'v':
                m_slice = maze[r_loc[0]:, r_loc[1]]
                # maze[r_loc[0]:, r_loc[1]] = process_slice(m_slice)
                # if m_slice[0] == '.':
                #     r_loc = (r_loc[0]+1, r_loc[1])
            case '<':
                m_slice = maze[r_loc[0], :r_loc[1] + 1][::-1]  # reverse for consistent processing
                maze[r_loc[0], :r_loc[1] + 1] = process_h_slice(m_slice)[::-1]
                if m_slice[0] == '.':
                    r_loc = (r_loc[0], r_loc[1]-1)
            case '>':
                m_slice = maze[r_loc[0], r_loc[1]:]
                maze[r_loc[0], r_loc[1]:] = process_h_slice(m_slice)
                if m_slice[0] == '.':
                    r_loc = (r_loc[0], r_loc[1] + 1)
        # print(dirn)
        # print_maze(maze)
    return maze


print_maze(expand_maze(base_maze))
processed_expanded = process_expanded(expand_maze(base_maze), base_directions)
print()
print_maze((processed_expanded))
#
print(process_h_slice(list(reversed(['#','#','.','.','.','.','[',']','@']))))
# print()
# print(process_h_slice(list(reversed(['#','#','.','[',']','.','[',']','@']))))