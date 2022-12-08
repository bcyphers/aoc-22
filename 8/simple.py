def solve(data):
    N = int(len(data) ** 0.5)

    # part one: which trees have a view?
    # O(N**2) time
    visible = set()

    for (x_step, y_step, r) in ((1, N, 1), (N, 1, 1),
                                (1, N, -1), (N, 1, -1)):
        for x in range(N):
            highest = -1
            for y in range(N)[::r]:
                i = x*x_step + y*y_step
                if data[i] > highest:
                    highest = data[i]
                    visible.add(i)

    print(len(visible))

    # part 2: which trees are visible from other trees?
    # O(N**3) I'm afraid
    scores = [1] * len(data)

    for x in range(N):
        for y in range(N):
            i = x + y*N
            right = [nx + y*N for nx in range(x+1, N)]
            left = [nx + y*N for nx in range(0, x)[::-1]]
            up = [x + ny*N for ny in range(y+1, N)]
            down = [x + ny*N for ny in range(0, y)[::-1]]

            for ahead in (right, left, up, down):
                count = 0
                while ahead:
                    count += 1
                    if data[ahead.pop(0)] >= data[i]:
                        break

                scores[i] *= count

    print(max(scores))


with open('input') as f:
    data = [int(v) for l in f for v in l.strip()]

test_input = '''
30373
25512
65332
33549
35390
'''

test_data = [int(v) for v in ''.join(test_input.strip().split())]

solve(test_data)
solve(data)
