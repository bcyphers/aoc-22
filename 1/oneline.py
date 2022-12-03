from functools import reduce

# part 1
print(
    reduce(
        lambda best, item: 
            (best[0], 0) if item is None else
                (max(best[0], best[1] + item), best[1] + item), 
        [int(l) if l.strip() else None for l in open('input')],
        (0, 0)
    )[0]
)

# part 2
print(
    sum(
        sorted(
            reduce(
                lambda elves, item: 
                    elves + [0] if item is None else
                        elves[:-1] + [elves[-1] + item],
                [int(l) if l.strip() else None for l in open('input')],
                [0]
            ) 
        )[-3:]
    )
)
