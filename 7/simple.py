with open('input') as f:
    lines = [l for l in f]

# store directory paths as tuples
ROOT = ('/',)
pwd = ROOT

# store contents of each dir indexed by full dir path
tree = {ROOT: []}

# build up `tree` dict
for l in lines:
    words = l.strip().split(' ')

    # walk through directory tree
    if words[0] == '$':
        if words[-1] == '/':
            pwd = ROOT
        elif words[-1] == '..':
            pwd = pwd[:-1]
        elif words[1] == 'cd':
            pwd += (words[-1],)

    # update branches in the tree
    elif words[0] == 'dir':
        d = pwd + (words[-1],)
        tree[pwd].append(d)
        tree[d] = []
    else:
        tree[pwd].append(int(words[0]))

# size of each dir indexed by full dir path
sizes = {}

# recursively calculate dir sizes
def get_size(node):
    if type(node) == int:
        return node

    global sizes
    sizes[node] = sum([get_size(n) for n in tree[node]])
    return sizes[node]

# build the size dict
get_size(('/',))

# part 1
print(sum(s for i, s in sizes.items() if s <= 100000))

# part 2
space_needed = 30000000 - (70000000 - sizes[('/',)])
print(min(s for i, s in sizes.items() if s >= space_needed))
