with open('input') as f:
    JETS = [1 if c == '>' else -1 for c in f.read().strip()]

# these are upside down to make y-indexing a little easier
ROCKS = [
    [[1,1,1,1]],
    [[0,1,0],
     [1,1,1],
     [0,1,0]],
    [[1,1,1],
     [0,0,1],
     [0,0,1]],
    [[1],
     [1],
     [1],
     [1]],
    [[1,1],
     [1,1]]
]

WIDTH = [max(len(s) for s in r) for r in ROCKS]

HEIGHT = [len(r) for r in ROCKS]

MAX_X = 7
ORIGIN = (2, 3)


# convert a rock's position to a bitstring for collision detection
def bitstring(x, y, rock, y_rng):
    out = ''
    for i in y_rng:
        if i < y or i >= y + HEIGHT[rock]:
            out += '0' * MAX_X
            continue
        for j in range(MAX_X):
            if j >= x and j < x + WIDTH[rock]:
                out += str(ROCKS[rock][i - y][j - x])
            else:
                out += '0'

    return int(out, 2)

# check if a rock collides with anything on the pile
def collide(x, y, rock, pile):
    for rx, ry, ri in pile:
        # if this rock is above the highest remaining rock, we're done checking
        if ry + HEIGHT[ri] < y:
            return False

        # otherwise, check if the two rocks collide
        y_rng = range(min(y, ry), max(y + HEIGHT[rock], ry + HEIGHT[ri]))
        bits1 = bitstring(x, y, rock, y_rng)
        bits2 = bitstring(rx, ry, ri, y_rng)

        if bits1 & bits2:
            return True

# keep the list of rocks sorted
def insert(x, y, rock, pile):
    i = 0
    for _, ry, ri in pile:
        if ry + HEIGHT[ri] <= y + HEIGHT[rock]:
            break
        i += 1

    pile.insert(i, (x, y, rock))


def pile_height(pile):
    return pile[0][1] + HEIGHT[pile[0][2]]


def simulate(num_rocks, loops=None):
    # x, y designates bottom left corner of current rock
    x, y = ORIGIN

    # index of current rock and jet
    rock = 0
    jet = 0

    # stores list of (position, rock index) for all rocks placed so far
    # sorted in descending order by position of the top of each rock
    pile = []

    while len(pile) < num_rocks:
        step = JETS[jet]
        # try to move based on jet
        # collision with left wall
        if x + step < 0:
            x = 0
        # collision with right wall
        elif x + step + WIDTH[rock] > MAX_X:
            x = MAX_X - WIDTH[rock]
        # collision with another rock
        elif not collide(x + step, y, rock, pile):
            x += step

        # now try to move down
        # collision with floor or with another rock
        if y - 1 < 0 or collide(x, y-1, rock, pile):
            # add old rock to the pile
            insert(x, y, rock, pile)

            # spawn a new rock
            rock = (rock + 1) % len(ROCKS)
            x = ORIGIN[0]
            y = pile_height(pile) + ORIGIN[1]
        else:
            y -= 1

        # on to the next jet
        jet = (jet + 1) % len(JETS)

        # we might want to stop after finishing a certain number of loops
        if jet == 0 and loops is not None:
            loops -= 1
            if loops == 0:
                return pile

    return pile

# Print out the pile
def output(pile):
    bits = [[0]*7 for i in range(pile[0][1] + HEIGHT[pile[0][2]])]
    for x, y, r in reversed(pile):
        for i in range(HEIGHT[r]):
            for j in range(WIDTH[r]):
                bits[y + i][x + j] |= ROCKS[r][i][j]

    for l in reversed(bits):
        print(''.join('#' if b else '.' for b in l))


# part 1
pile = simulate(2022)
print(pile_height(pile))

# part 2
total = 1000000000000
pile1 = simulate(total, loops=1)
pile2 = simulate(total, loops=2)
mod = len(pile2) - len(pile1)
div = (total - len(pile1)) // mod
pile3 = simulate(len(pile1) + (total - len(pile1)) % mod)

p1h = pile_height(pile1)
p2h = pile_height(pile2) - p1h
p3h = pile_height(pile3) - p1h

print(p2h * div + p1h + p3h)
