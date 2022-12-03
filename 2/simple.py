with open('input') as f:
    lines = [l.split() for l in f]

# part 1: given both inputs
points = 0

for l in lines:
    # opponent's play (0=rock, 1=paper, 2=scissors)
    a = ord(l[0]) - ord('A')

    # your play
    b = ord(l[1]) - ord('X')

    # desired outcome (0=lose, 1=draw, 2=win)
    c = (b - a + 1) % 3

    points += b + 1 + c * 3

print(points)

# part 2: given opp input and result
points = 0

for l in lines:
    # opponent's play (0=rock, 1=paper, 2=scissors)
    a = ord(l[0]) - ord('A')

    # desired outcome (0=lose, 1=draw, 2=win)
    b = ord(l[1]) - ord('X')

    # your play
    c = (a + b - 1) % 3

    points += c + 1 + b * 3

print(points)
