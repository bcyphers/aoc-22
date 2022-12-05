print(*[
    sum(
        # apply boolean function to each pair of ranges in the input
        map(
            func,
            # sort the two ranges by start point
            [
                tuple(sorted(
                    [tuple(map(int, i.split('-'))) for i in l.split(',')],
                    key=lambda e: e[0]
                )) for l in open('input')
            ]
        )
    ) for func in (
        # function for part 1: containment?
        lambda e: e[0][0] == e[1][0] or e[1][1] <= e[0][1],
        # function for part 2: any overlap?
        lambda e: e[1][0] <= e[0][1]
    )
])
