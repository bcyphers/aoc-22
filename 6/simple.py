def find_n_unique(buffer, n):
    for i in range(n, len(buffer)):
        if len(set(buffer[i-n:i])) == n:
            print(i)
            return

buffer = open('input').read()

# part 1
find_n_unique(buffer, 4)
# part 2
find_n_unique(buffer, 14)
