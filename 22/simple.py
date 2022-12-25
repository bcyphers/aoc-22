import re

with open('input') as f:
    data, path = f.read().split('\n\n')

data = data.split('\n')

# part 1
def wrap_1(r, c, facing):
    if facing & 1 == 0:
        c = (len(data[r])-1) * (facing >> 1)
        while data[r][c] == ' ':
            c += 1 - facing
    else:
        r = (len(data)-1) * (facing >> 1)
        while len(data[r]) <= c or data[r][c] == ' ':
            r += 1 - (facing & 2)

    return (r, c, facing)


# part 2
def wrap_2(r, c, facing):
    pass


r = 0
c = data[0].index('.')
# 0 = right, 1 = down, 2 = left, 3 = up
facing = 0

path = re.findall('(\d+|\w)', path)
for p in path:
    print(p)
    if p == 'R':
        facing = (facing + 1) % 4
    elif p == 'L':
        facing = (facing - 1) % 4
    else:
        for _ in range(int(p)):
            new_r, new_c = (r, c)

            if facing & 1 == 0:
                new_c += 1 - facing
                # check for out of bounds
                if not 0 <= new_c < len(data[r]) or data[r][new_c] == ' ':
                    new_r, new_c, new_facing = wrap(r, new_c, facing)
            else:
                new_r += 1 - (facing & 2)
                # check for out of bounds
                if not 0 <= new_r < len(data) or len(data[new_r]) <= c or \
                        data[new_r][c] == ' ':
                    new_r, new_c, new_facing = wrap(new_r, c, facing)

            # check for wall
            if data[new_r][new_c] == '#':
                break

            r, c, facing = (new_r, new_c, new_facing)
    print(r, c, facing)

print((r+1) * 1000 + (c+1) * 4 + facing)
