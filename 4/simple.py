contained = 0
overlap = 0

# goal: minimize comparisons

with open('input') as f:
    for l in f:
        a, b = [tuple(map(int, i.split('-'))) for i in l.split(',')]

        # order the two ranges by start point
        (s1, e1), (s2, e2) = (a, b) if a[0] <= b[0] else (b, a)

        # if the second range starts before the first range ends, there is an
        # overlap
        if s2 <= e1:
            overlap += 1

            # if the starts are the same or the second range ends before the
            # first range does, there is containment
            if s1 == s2 or e2 <= e1:
                contained += 1

print(contained, overlap)


