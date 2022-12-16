with open('input') as f:
    data = []
    for i, l in enumerate(f):
        if 'S' in l:
            start = (i, l.find('S'))
        if 'E' in l:
            end = (i, l.find('E'))

        data.append(l.strip())

M = len(data)
N = len(data[0])

# part 1
def search(start, end, traversable):
    paths = [[start]]
    seen = set([start])
    while paths:
        path = paths.pop(0)
        r, c = path[-1]
        for n in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= n[0] < M and 0 <= n[1] < N and \
                    n not in seen and \
                    traversable(data[r][c], data[n[0]][n[1]]):
                if data[n[0]][n[1]] == end:
                    return path
                seen.add(n)
                paths.append(path + [n])

p1_test = lambda c1, c2: c1 in 'yz' if c2 == 'E' else ord(c2) - ord(c1.lower()) <= 1

p2_test = lambda c1, c2: p1_test(c2, c1)

path = search(start, 'E', p1_test)
print(len(path))
path = search(end, 'a', p2_test)
print(len(path))
