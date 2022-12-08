# these only work because of a few assumptions:
#   1. Each directory is only visited once
#   2. After a directory is visited, all of its subdirectories will be visited
#   before visiting anything else
#   3. `ls` is only called once for each directory

# part 1
print(
    (lambda lines:
        sum(
            s for s in map(
                # function receives the index of a `ls` call, finds total size
                # of that directory
                lambda i: sum([
                    # add up all the file sizes we see between now and the point
                    # where we exit the directory
                    int(lines[j].split(' ')[0]) for j in range(i, next(
                            # find index of line where we exit this directory
                            filter(
                                # Value for each index is depth relative to
                                # position at index i.
                                lambda ii:
                                    ii == len(lines) - 1 or
                                    (lines[ii] == '$ cd /') or
                                    sum(
                                        # look at all the cd commands in the
                                        # rest of the input. add 1 if going
                                        # deeper, -1 if backing out.
                                        (-1 if l.split(' ')[-1] == '..' else 1)
                                        for l in lines[i+1:ii] if l.startswith('$ cd')
                                    ) < 0,
                                range(i, len(lines))
                            )
                        )) if lines[j].split(' ')[0].isdecimal()
                    ]),
                [i for i, l in enumerate(lines) if l == '$ ls']
            ) if s <= 100000
        )
    )([l.strip() for l in open('input')])
)

# part 2
print(
    (lambda lines:
        min(
            s for s in map(
                lambda i: sum([
                    int(lines[j].split(' ')[0]) for j in range(i, next(
                            filter(
                                lambda ii:
                                    ii == len(lines) - 1 or
                                    (lines[ii] == '$ cd /') or
                                    sum(
                                        (-1 if l.split(' ')[-1] == '..' else 1)
                                        for l in lines[i+1:ii] if l.startswith('$ cd')
                                    ) < 0,
                                range(i, len(lines))
                            )
                        )) if lines[j].split(' ')[0].isdecimal()
                    ]),
                [i for i, l in enumerate(lines) if l == '$ ls']
            ) if s >= (3e7 - (7e7 - sum(
                map(
                    lambda l: int(l.split()[0]),
                    filter(lambda l: l[0].isdigit(), lines)
                )
            )))
        )
    )([l.strip() for l in open('input')])
)
