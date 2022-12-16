import re

paths = []
with open('input') as f:
    for l in f:
        paths.append(re.findall('(\d+),(\d+)', l))

rock = set()
for path in paths:
    for i in range(len(path) - 1):
        x1, y1 = map(int, path[i])
        x2, y2 = map(int, path[i+1])

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                rock.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                rock.add((x, y1))

bottom = max(list(zip(*rock))[1])
origin = (500, 0)
sand = set()

# part 1
while True:
    x, y = origin
    while y <= bottom:
        if (x, y+1) not in rock | sand:
            y += 1
        elif (x-1, y+1) not in rock | sand:
            x -= 1
            y += 1
        elif (x+1, y+1) not in rock | sand:
            x += 1
            y += 1
        else:
            sand.add((x, y))
            break

    if y > bottom:
        break

print(len(sand))

sand = set()
floor = bottom + 2

# part 2
while True:
    x, y = origin
    while True:
        if y+1 >= floor:
            sand.add((x, y))
            print(x, y)
            break

        if (x, y+1) not in rock | sand:
            y += 1
        elif (x-1, y+1) not in rock | sand:
            x -= 1
            y += 1
        elif (x+1, y+1) not in rock | sand:
            x += 1
            y += 1
        else:
            sand.add((x, y))
            break

    if (x, y) == origin:
        break

print(len(sand))

with open('sand.txt', 'w') as f:
    X = list(zip(*rock))[0]
    left = min(X)
    width = max(X) - left

    for r in range(bottom + 1):
        line = ''
        for i in range(width):
            c = i + left
            if (c, r) in rock:
                line += '#'
            elif (c, r) in sand:
                line += 'o'
            else:
                line += '.'
        f.write(line + '\n')
