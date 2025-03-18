import itertools

with open("./data/input_07.txt") as f:
    lines = [line.strip().split(':') for line in f]
    lines = [(int(a), [int(n) for n in b.strip().split()]) for a, b in lines]


def find_eqn(total, numbers, operators):
    for comb in itertools.product(operators, repeat=len(numbers)-1):
        t = numbers[0]
        for sign, num in zip(comb, numbers[1:]):
            match sign:
                case '+':
                    t += num
                case '*':
                    t *= num
                case '||':
                    t = int(str(t) + str(num))
        if t == total:
            return True
    return False


print(sum(total for total, numbers in lines if find_eqn(total, numbers, ['+', '*'])))
print(sum(total for total, numbers in lines if find_eqn(total, numbers, ['+', '*', '||'])))
