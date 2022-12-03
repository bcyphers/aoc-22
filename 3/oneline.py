# part 1
print(
    sum([
            (set(bag[:len(bag)//2]) & set(bag[len(bag)//2:])).pop() 
            for bag in [
                [ord(c.lower()) - ord('a') + c.isupper() * 26 + 1 for c in l.strip()]
                for l in open('input')
            ]
        ]
    )
)

from functools import reduce
import string

# part 2
print(
    reduce(
        lambda s, b:
            (s[0], s[1] & b, s[2] + 1) if s[2] < 2 else 
                (s[0] + s[1].pop(), b, 0),
        [{ord(c.lower()) - ord('a') + c.isupper() * 26 + 1 for c in l.strip()}
            for l in open('input')] + [set()],
        (0, set(range(1, 53)), -1)
    )[0]
)
