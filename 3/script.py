# load data
with open('input') as f:
    lines = [l.strip() for l in f]

# get priority of item
# a-z = 1-26, A-Z = 27-52
priority = lambda i: ord(i.lower()) - ord('a') + i.isupper() * 26 + 1


# part 1: priority of misplaced items
total = 0

for l in lines:
    # find the character that appears in both halves of the string
    item = (set(l[:len(l)//2]) & set(l[len(l)//2:])).pop()

    total += priority(item)

print(total)


# part 2: priority of shared items
total = 0

# iterate over groups of 3
for i in range(0, len(lines), 3):
    # find the char in all 3 lines using set intersection
    item = (set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()

    total += priority(item)

print(total)
