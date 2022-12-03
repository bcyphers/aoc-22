elves = [0]

with open('input') as f:
    for l in f:
        if l.strip():
            elves[-1] += int(l)
        else:
            elves.append(0)

# find the most food held by any elf
print(max(elves))

# find the amount of food held by the top 3 elves
print(sum(sorted(elves)[-3:]))
