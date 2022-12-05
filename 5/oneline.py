from functools import reduce

print(*[
    ''.join(
        s[-1] for s in reduce(
            # apply the actions to the stack
            func,
            # load the list of instructions
            [
                tuple([int(e) for e in l.split()[1::2]])
                for l in open('input') if l[0] == 'm'
            ],
            # generate the initial state of the stacks
            [
                [
                    e[i] for e in [
                        l[1::4] for l in
                        open('input').read().split('\n 1')[0].strip().split('\n')
                    ][::-1] if e[i].strip()
                ] for i in range(9)
            ]
        )
    ) for func in (
        # part 1
        lambda state, act: [
            state[i][:-act[0]] if i == act[1]-1 else (
                state[i] + state[act[1]-1][:-act[0]-1:-1]
                    if i == act[2]-1 else state[i][:]
            )
            for i in range(9)
        ],
        # part 2
        lambda state, act: [
            state[i][:-act[0]] if i == act[1]-1 else (
                state[i] + state[act[1]-1][-act[0]:]
                    if i == act[2]-1 else state[i][:]
            )
            for i in range(9)
        ]
    )
])
