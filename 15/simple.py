import re
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle, Polygon

sensors = []
#with open('test') as f:
with open('input') as f:
    for l in f:
        s, b = re.findall('x=(\-?\d+), y=(\-?\d+)', l)
        sx, sy = map(int, s)
        bx, by = map(int, b)

        dist = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, dist))

MAX = 4000000
#MAX = 20

y = 2000000
#y = 10

## Part 1
ranges = []
for s in sorted(sensors, key=lambda s: s[0]):
    # does the sensor's range touch the row?
    if abs(s[1] - y) <= s[2]:
        dist = s[2] - abs(s[1] - y)

        # does it intersect with the previous range?
        if len(ranges) and s[0] - dist <= ranges[-1][1]:
            x1, x2 = ranges.pop(-1)
            ranges.append((min(x1, s[0] - dist), max(x2, s[0] + dist)))

        # if this is the first intersecting range, or it doesn't intersect with
        # the previous range, add it to the list
        else:
            ranges.append((s[0] - dist, s[0] + dist))

print(sum(map(lambda r: r[1] - r[0], ranges)))


## Part 2

# do two line segments intersect? if so, where?
# given that s1 and s2 are perpendicular, and that
# slope(s1) = 1 and slope(s2) = -1
def intersect(s1, s2):
    ax1, ay1, ax2, ay2 = s1
    bx1, by1, bx2, by2 = s2

    # get the point where the two lines meet
    x = ((by2 + bx2) - (ay1 - ax1)) // 2
    y = x + (ay1 - ax1)

    # is this point within both segments?
    if max(ax1, bx1) <= x <= min(ax2, bx2):
        return x, y

    return False

# get line segments that border a sensor's bounding box
def get_segments(s):
    return [
        # first two are slope=1
        (s[0] - s[2] - 1, s[1], s[0], s[1] + s[2] + 1),
        (s[0], s[1] - s[2] - 1, s[0] + s[2] + 1, s[1]),
        # next two are slope=-1
        (s[0] - s[2] - 1, s[1], s[0], s[1] - s[2] - 1),
        (s[0], s[1] + s[2] + 1, s[0] + s[2] + 1, s[1])
    ]

# find all points where border lines intersect
points = set()
for i in range(len(sensors)):
    a, b, c, d = get_segments(sensors[i])

    for j in range(i+1, len(sensors)):
        e, f, g, h = get_segments(sensors[j])

        for pair in ((a, g), (b, g), (a, h), (b, h),
                     (e, c), (f, c), (e, d), (f, d)):
            point = intersect(*pair)
            if point:
                points.add(point)


# check all the intersection points to see if any are in the box and out of
# range of all other sensors
for x, y in points:
    if x < 0 or x > MAX or y < 0 or y > MAX:
        continue
    for s in sensors:
        if abs(s[0] - x) + abs(s[1] - y) <= s[2]:
            break
    else:
        # this is the one
        print(x * 4000000 + y)
