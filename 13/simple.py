import functools

with open('input') as f:
    pairs = []
    for pair in f.read().split('\n\n'):
        pairs.append([eval(l) for l in pair.strip().split('\n')])

def compare(l1, l2):
    for i in range(len(l1)):
        l = l1[i]
        if len(l2) <= i:
            return False
        r = l2[i]

        if type(l) is list:
            if type(r) is not list:
                r = [r]
        elif type(r) is list:
            l = [l]
        else:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue

        c = compare(l, r)
        if c is not None:
            return c

    if len(l2) > len(l1):
        return True

total = 0
for i, (l1, l2) in enumerate(pairs):
    if compare(l1, l2):
        total += i + 1

print(total)

all_packets = [[[6]], [[2]]]
for p in pairs:
    all_packets.extend(p)

srt = sorted(all_packets, key=functools.cmp_to_key(
    lambda a, b: 0 if compare(a, b) is None else (
        -1 if compare(a, b) is True else 1
    )
))

print((srt.index([[6]]) + 1) * (srt.index([[2]]) + 1))
