class Config:
    def __init__(self, a, b, p) -> None:
        self.a = a
        self.b = b
        self.p = p

    def solve(self) -> tuple:
        a_n = self.a[0] * self.b[1] - self.a[1] * self.b[0]
        p_n = self.p[0] * self.b[1] - self.p[1] * self.b[0]
        a, a_m = divmod(p_n, a_n)
        b, b_m = divmod((self.p[0] - a*self.a[0]), self.b[0])
        return (a, b) if a_m == 0 and b_m == 0 else (0, 0)


with open("./data/input_13.txt") as f:
    configs = []
    while True:
        lines = [f.readline().strip() for _ in range(4)]
        if not any(lines):
            break
        al = [int(x.split('+')[1]) for x in lines[0].split(":")[1].split(',')]
        bl = [int(x.split('+')[1]) for x in lines[1].split(":")[1].split(',')]
        pl = [int(x.split('=')[1]) for x in lines[2].split(":")[1].split(',')]
        configs.append(Config(al, bl, pl))

print(sum(3*a + b for c in configs for a, b in [c.solve()]))

for c in configs:
    c.p = [x + 10000000000000 for x in c.p]
print(sum(3*a + b for c in configs for a, b in [c.solve()]))
