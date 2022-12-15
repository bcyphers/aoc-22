class Monkey(object):
    def __init__(self, data):
        _, items, op, test, t, f = d.split('\n')
        opcode = op.split('new = ')[1]
        self.func = lambda old: eval(opcode)
        self.items = list(map(int, items.split(': ')[1].split(', ')))
        self.divisor = int(test.split()[-1])
        self.true = int(t.split()[-1])
        self.false = int(f.split()[-1])
        self.inspections = 0

monkeys = []
with open('input') as f:
    data = f.read().strip().split('\n\n')
    for d in data:
        monkeys.append(Monkey(data))

lcd = 1
for m in monkeys:
    lcd *= m.divisor

def part_1():
    for _ in range(20):
        for m in monkeys:
            while m.items:
                it = m.items.pop(0)
                new = m.func(it) // 3
                next_m = m.false if new % m.divisor else m.true
                monkeys[next_m].items.append(new)
                m.inspections += 1

def part_2():
    for _ in range(10000):
        for m in monkeys:
            while m.items:
                it = m.items.pop(0)
                new = m.func(it) % lcd
                next_m = m.false if new % m.divisor else m.true
                monkeys[next_m].items.append(new)
                m.inspections += 1

part_2()
m1, m2 = sorted([m.inspections for m in monkeys])[-2:]
print(m1 * m2)
