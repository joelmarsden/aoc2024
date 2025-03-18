with open("./data/input_17.txt") as f:
    A, B, C = (int(f.readline().strip().split(':')[1]) for _ in range(3))
    f.readline()
    tape = list(map(int, f.readline().strip().split(':')[1].split(',')))


def run_program(a, b, c, p) -> (list, int, int, int):

    def combo_operand(operand) -> int:
        assert 0 <= operand <= 7
        return [0, 1, 2, 3, a, b, c][operand]

    i_pointer = 0
    output = []

    while i_pointer < len(p):
        opcode, op = p[i_pointer], p[i_pointer+1]
        combo_op = combo_operand(op)
        match opcode:
            case 0:  a = a // (2 ** combo_op)
            case 1:  b = b ^ op
            case 2:  b = combo_op % 8
            case 3:
                if a != 0:
                    i_pointer = op
                    continue
            case 4:  b = b ^ c
            case 5:  output.append(combo_op % 8)
            case 6:  b = a // (2 ** combo_op)
            case 7:  c = a // (2 ** combo_op)
        i_pointer += 2
    return output, a, b, c


print(run_program(A, B, C, tape))

print(run_program(117440, 0, 0, [0, 3, 5, 4, 3, 0]))
