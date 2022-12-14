class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        return Vector(self.x - other[0], self.y - other[1])

    def __getitem__(self, key):
        return self.x if key == 0 else self.y

    def __str__(self):
        return '%d, %d' % (self.x, self.y)

    def __abs__(self):
        return pow(self.x**2 + self.y**2, 0.5)

    def dir(self):
        return Vector(self.x / abs(self.x or 1), self.y / abs(self.y or 1))


DIRS = {'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)}


def simulate_rope(steps, ropelen):
    rope = [Vector(0, 0) for i in range(ropelen)]
    trail = set([str(rope[-1])])
    for d, n in steps:
        for _ in range(int(n)):
            rope[0] += DIRS[d]
            for i in range(ropelen - 1):
                dif = rope[i] - rope[i+1]
                if abs(dif) >= 2:
                    rope[i+1] += dif.dir()

            trail.add(str(rope[-1]))

    print(len(trail))


with open('input') as f:
    steps = [l.strip().split(' ') for l in f]

# part 1
simulate_rope(steps, 2)
# part 2
simulate_rope(steps, 10)
