from math import ceil


lines = open('aoc13.txt').read().splitlines()
t = int(lines[0])
buses = list(map(int, lines[1].replace('x,', '').split(',')))
earliest_id, min_wait = 0, 1000000000
for bus_id in buses:
    wait = ceil(t / bus_id) * bus_id - t
    if wait < min_wait:
        min_wait = wait
        earliest_id = bus_id

print(earliest_id * min_wait)
