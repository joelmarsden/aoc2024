import itertools


def load_data(file_path):
    # Ensure consistent path handling
    if not file_path.startswith('./data/'):
        file_path = './data/' + file_path.split('/')[-1]

    with open(file_path) as f:
        lines = [line.strip().split(':') for line in f]
        return [(int(a), [int(n) for n in b.strip().split()]) for a, b in lines]


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


def part1(data):
    return sum(total for total, numbers in data if find_eqn(total, numbers, ['+', '*']))


def part2(data):
    return sum(total for total, numbers in data if find_eqn(total, numbers, ['+', '*', '||']))


if __name__ == "__main__":
    data = load_data("./data/input_07.txt")
    print(part1(data))
    print(part2(data))
