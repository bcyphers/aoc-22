import re
import inspect

values = {}
ops = {}


def resolve_1(solved, unsolved, op, v1, v2):
    for v in [v1, v2]:
        if v in unsolved:
            args = unsolved.pop(v)
            ans = resolve_1(solved, unsolved, *args)
            solved[v] = ans

    f = lambda a, b: eval('a %s b' % op)
    return f(solved[v1], solved[v2])


def resolve_2(solved, unsolved, op, v1, v2):
    print(v1, op, v2)
    for v in [v1, v2]:
        if v in unsolved:
            args = unsolved.pop(v)
            ans = resolve_2(solved, unsolved, *args)
            solved[v] = ans

    if v1 == 'humn' or type(solved[v1]) == list:
        if op == '+':
            f = lambda x: x - solved[v2]
        elif op == '-':
            f = lambda x: x + solved[v2]
        elif op == '*':
            f = lambda x: x / solved[v2]
        elif op == '/':
            f = lambda x: x * solved[v2]
    elif v2 == 'humn' or type(solved[v2]) == list:
        if op == '+':
            f = lambda x: x - solved[v1]
        elif op == '-':
            f = lambda x: solved[v1] - x
        elif op == '*':
            f = lambda x: x / solved[v1]
        elif op == '/':
            f = lambda x: solved[v1] / x

    if v1 == 'humn' or v2 == 'humn':
        return [f]
    elif type(solved[v1]) == list:
        return [f] + solved[v1]
    elif type(solved[v2]) == list:
        return [f] + solved[v2]
    else:
        f = lambda a, b: eval('a %s b' % op)
        return f(solved[v1], solved[v2])


def resolve_stack(funcs, x):
    for f in funcs:
        x = f(x)

    return x


with open('input') as f:
    for l in f:
        # each variable is only assigned once
        m1 = re.match('(\w+): (\d+)', l)
        if m1:
            values[m1.groups()[0]] = int(m1.groups()[1])
            continue

        key, v1, op, v2 = re.match('(\w+): (\w+) ([+\-*\/]) (\w+)', l).groups()
        ops[key] = (op, v1, v2)


# part 1
print(resolve_1(values.copy(), ops.copy(), *ops['root']))

# part 2
del values['humn']
_, v1, v2 = ops['root']
a = resolve_2(values, ops, *ops[v1])
b = resolve_2(values, ops, *ops[v2])

if type(a) in [int, float]:
    print(resolve_stack(b, a))
else:
    print(resolve_stack(a, b))
