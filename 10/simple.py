X = [1]
with open('input') as f:
    for l in f:
        X.append(X[-1])
        if l.startswith('addx'):
            X.append(X[-1] + int(l.split()[1]))

# part 1
val = 0
for i in range(19, 220, 40):
    val += (i+1) * X[i]

print(val)

# part 2
out = ''
for r in range(6):
    for c in range(40):
        i = r * 40 + c
        if abs(X[i] - c) <= 1:
            out += '#'
        else:
            out += '.'
    out += '\n'

print(out)
