from operator import mul
from functools import reduce

map_arr = open('aoc3.txt').read().splitlines()
# part 1
t = 0
for r in range(1, len(map_arr)):
    c = (r * 3) % len(map_arr[0])
    if map_arr[r][c] == '#':  # Tree
        t += 1
print(t)
# part 2
vals = []
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
for R, C in slopes:
    t = 0
    for r in range(R, len(map_arr), R):
        c = (r * C // R) % len(map_arr[0])
        if map_arr[r][c] == '#':  # Tree
            t += 1
    vals.append(t)

print(reduce(mul, vals, 1))  # product of list
