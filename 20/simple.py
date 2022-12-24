DKEY = 811589153

class IntObj(object):
    def __init__(self, val):
        if type(val) == int:
            self.value = val
        else:
            self.value = int(val)

    def __imul__(self, val):
        self.value *= val
        return self


def part_1(data_in):
    data_out = data_in[:]
    mod = len(data_in) - 1

    for i in data_in:
        j = data_out.index(i)
        v = data_out.pop(j)
        data_out.insert((j + v.value) % mod, v)

    result = [d.value for d in data_out]
    start = result.index(0)
    out = sum(result[(i + start) % len(data_in)] for i in [1000, 2000, 3000])

    print(out)


def part_2(data_in):
    data_in = data_in[:]
    for d in data_in:
        d *= DKEY

    data_out = data_in[:]
    mod = len(data_in) - 1

    for _ in range(10):
        for i in data_in:
            j = data_out.index(i)
            v = data_out.pop(j)
            data_out.insert((j + v.value) % mod, v)

    result = [d.value for d in data_out]
    start = result.index(0)
    out = sum(result[(i + start) % len(data_in)] for i in [1000, 2000, 3000])

    print(out)


with open('input') as f:
    data_in = [IntObj(l) for l in f]

test_in = list(map(IntObj, [1, 2, -3, 3, -2, 0, 4]))

part_1(data_in)
part_2(data_in)
