# part 1
print(
    sum([b + 1 + ((b - a + 1) % 3) * 3
         for a, b in [(ord(l.split()[0]) - ord('A'), ord(l.split()[1]) - ord('X')) 
                      for l in open('input')]]
     )
)

# part 2
print(
    sum([b * 3 + ((a + b - 1) % 3) + 1
         for a, b in [(ord(l.split()[0]) - ord('A'), ord(l.split()[1]) - ord('X')) 
                      for l in open('input')]]
     )
)
