with open('input') as f:
    lines = [l for l in f]

# load in stack data
stacks = [[] for i in range(9)]
for i, l in enumerate(lines):
    if '[' not in l:
        break
    for ii in range(9):
        stacks[ii].append(l[ii*4 + 1])

for j in range(len(stacks)):
    stacks[j] = [e for e in reversed(stacks[j]) if e.strip()]

for l in lines[i + 2:]:
    # process moves
    n, src, dest = [int(e) for e in l.split()[1::2]]

    # part 1 logic
    #for ii in range(n):
        #stacks[dest-1].append(stacks[src-1].pop(-1))

    # part 2 logic
    stacks[dest-1].extend(stacks[src-1][-n:])
    stacks[src-1] = stacks[src-1][:-n]

print(''.join([s[-1] for s in stacks]))
