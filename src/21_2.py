from numpy.f2py.auxfuncs import throw_error
from itertools import product

with open("./data/input_21_ex.txt") as f:
    codes = [list(l.strip()) for l in f]

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


def navigate_keypad(matrix, start, end, prefer_v=True):

    start_row, start_col = find_coordinates(matrix, start)
    end_row, end_col = find_coordinates(matrix, end)

    directions = []
    if prefer_v:
        directions.extend(nav_v(start_row, end_row))
        directions.extend(nav_h(start_col, end_col))
    else:
        directions.extend(nav_h(start_col, end_col))
        directions.extend(nav_v(start_row, end_row))
    return directions + ['A']


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
        print(f'\t3.1 ({fr},{to}), {nk}')
        ins3.extend(nk)
    print(3,ins3)
    return ins3


# def code_to_ins_2(code):
#     ins = []
#     c = ['A'] + code
#     for fr, to in zip(c, c[1:]):
#         l2 = navigate_keypad_2(keypad, fr, to)
#         if not ins:
#             ins = l2
#         else:
#             ins = [x + y for x, y in product(ins, l2)]



part1 = 0
for code in codes:
    ins = code_to_ins(code)
    n = int(''.join(code[0:len(code)-1]))
    l = len(ins)
    print(l,'*',n)
    part1 += n*l
print(part1)