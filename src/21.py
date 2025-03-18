from numpy.f2py.auxfuncs import throw_error
from itertools import product

with open("./data/input_21_ex.txt") as f:
    codes = [list(l.strip()) for l in f]

# print(codes)

keypad = [
    ['7',  '8', '9'],
    ['4',  '5', '6'],
    ['1',  '2', '3'],
    [None, '0', 'A']
]

dir_keypad = [
    [None, '^', 'A'],
    ['<',  'v', '>']
]

def find_coordinates(matrix, value):
    for i, row in enumerate(matrix):
        if value in row:
            return i, row.index(value)
    return None


def nav_v(start_row, end_row):
    directions = []
    while start_row > end_row:
        directions.append("^")
        start_row -= 1
    while start_row < end_row:
        directions.append("v")
        start_row += 1
    return directions


def nav_h(start_col, end_col):
    directions = []
    while start_col > end_col:
        directions.append("<")
        start_col -= 1
    while start_col < end_col:
        directions.append(">")
        start_col += 1
    return directions


def navigate_keypad(matrix, start, end):
    """Determine the step-by-step navigation directions from start to end."""
    start_coords = find_coordinates(matrix, start)
    end_coords = find_coordinates(matrix, end)

    if not start_coords or not end_coords:
        throw_error(f"One or both values not found in the matrix: {start}, {end}")

    start_row, start_col = start_coords
    end_row, end_col = end_coords

    directions = []
    directions.extend(nav_v(start_row, end_row))
    directions.extend(nav_h(start_col, end_col))
    return directions + ['A']


def navigate_keypad_2(matrix, start, end):
    """Determine the step-by-step navigation directions from start to end."""
    start_coords = find_coordinates(matrix, start)
    end_coords = find_coordinates(matrix, end)

    if not start_coords or not end_coords:
        throw_error(f"One or both values not found in the matrix: {start}, {end}")

    start_row, start_col = start_coords
    end_row, end_col = end_coords

    ret = []
    directions = []
    directions.extend(nav_v(start_row, end_row))
    directions.extend(nav_h(start_col, end_col))
    directions = directions + ['A']
    ret.append(directions)

    directions = []
    directions.extend(nav_h(start_col, end_col))
    directions.extend(nav_v(start_row, end_row))
    directions = directions + ['A']
    ret.append(directions)

    return ret


def to_ins_str(ins):
    return ''.join(map(str, ins))


def code_to_ins(code):
    ins = []
    c = ['A'] + code
    for fr, to in zip(c, c[1:]):
        ins.extend(navigate_keypad(keypad, fr, to))

    print(1,ins)
    # robot -> dir_keypad
    ins2 = []
    c = ['A'] + ins
    for fr, to in zip(c, c[1:]):
        nk = navigate_keypad(dir_keypad, fr, to)
        print(f'\t2.1 ({fr},{to}), {nk}')
        ins2.extend(nk)
    print(2,ins2)
    # robot -> dir_keypad
    ins3 = []
    c = ['A'] + ins2
    for fr, to in zip(c, c[1:]):
        nk = navigate_keypad(dir_keypad, fr, to)
        print('\t3.1', nk)
        ins3.extend(nk)
    print(3,ins3)
    return ins3


def code_to_ins_2(code):
    ins = []
    c = ['A'] + code
    for fr, to in zip(c, c[1:]):
        l2 = navigate_keypad_2(keypad, fr, to)
        if not ins:
            ins = l2
        else:
            ins = [x + y for x, y in product(ins, l2)]

    # robot -> dir_keypad
    res2 = []
    for c in ins:
        ins2 = []
        c = ['A'] + c
        for fr, to in zip(c, c[1:]):
            ins2.extend(navigate_keypad(dir_keypad, fr, to))
        res2.append(ins2)

    # robot -> dir_keypad
    res3 = []
    for c in res2:
        ins3 = []
        c = ['A'] + c
        for fr, to in zip(c, c[1:]):
            ins3.extend(navigate_keypad(dir_keypad, fr, to))
        res3.append(ins3)

    return min(res3, key=len)

part1 = 0
for code in codes:
    ins = code_to_ins(code)
    n = int(''.join(code[0:len(code)-1]))
    l = len(ins)
    print(l,'*',n)
    part1 += n*l
print(part1)

print()
part1 = 0
for code in codes:
    ins = code_to_ins_2(code)
    n = int(''.join(code[0:len(code)-1]))
    l = len(ins)
    print(l,'*',n)
    part1 += n*l
print(part1)