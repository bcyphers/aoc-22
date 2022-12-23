from collections import defaultdict

class Vector(tuple):
    def __new__(cls, vals):
        return tuple.__new__(cls, vals)

    def __add__(self, vec):
        if not len(self) == len(vec):
            raise IndexError('Vectors must be the same length')

        return Vector([self[i] + vec[i] for i in range(len(self))])

    def __sub__(self, vec):
        if not len(self) == len(vec):
            raise IndexError('Vectors must be the same length')

        return Vector([self[i] - vec[i] for i in range(len(self))])


class OneHot(Vector):
    def __new__(cls, dim, vals):
        return Vector.__new__(cls, [1 if i in vals else 0 for i in range(dim)])


# load input
with open('input') as f:
    voxels = set([Vector([int(x) for x in l.split(',')]) for l in f])

norms = [OneHot(3, [i]) for i in range(3)]

## Part 1

def find_neighbors(voxels):
    # how many neighbors does each voxel have?
    neighbors = {v: 0 for v in voxels}

    # generate 3 lists of the voxels, one sorted by each axis
    axes = [((i+2) % 3, sorted(voxels,
                               key=lambda v: (v[i], v[(i+1)%3], v[(i+2)%3])))
            for i in range(3)]

    # find neighbors on each axis
    for i, axis in axes:
        for j, v in enumerate(axis):
            # check if there are any voxels directly to the left or right
            if j > 0 and v - norms[i] == axis[j-1]:
                neighbors[v] += 1
            if j+1 < len(axis) and v + norms[i] == axis[j+1]:
                neighbors[v] += 1

    return neighbors

total_sa = sum([6-n for n in find_neighbors(voxels).values()])
print(total_sa)

## Part 2
# check if any of the empty spaces we counted are totally enclosed by voxels
# start by enumerating all spaces within the shape's bounding cube that aren't
# in the shape
# next, use BFS to cull all spaces that are reachable from the outside
def find_empty_space():
    MIN = -1
    X, Y, Z = zip(*voxels)
    MAX = (max(X) + 1, max(Y) + 1, max(Z) + 1)

    enclosed = set()
    for x in range(MIN, MAX[0] + 1):
        for y in range(MIN, MAX[1] + 1):
            for z in range(MIN, MAX[2] + 1):
                v = Vector((x, y, z))
                if v not in voxels:
                    enclosed.add(v)

    leads = [Vector(MAX)]

    while len(leads):
        v = leads.pop(0)
        for d in norms:
            vneg = v - d
            vpos = v + d
            if vneg in enclosed:
                enclosed.remove(vneg)
                leads.append(vneg)
            if vpos in enclosed:
                enclosed.remove(vpos)
                leads.append(vpos)

    return enclosed

# now, find the surface area of the enclosed shape(s), and subtract it from our
# total surface area from earlier
enclosed = find_empty_space()
interior_sa = sum([6-n for n in find_neighbors(enclosed).values()])
print(total_sa - interior_sa)

