from math import ceil

# part 1
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

# part 2
# Generate list of (a, b) pairs such that x is congruent to a mod b
# I'm passing this list into some Chinese remainder theorem code I wrote a while back
buses = lines[1].split(',')
pairs = [(-i, int(bus_id)) for i, bus_id in enumerate(buses) if bus_id != 'x']
print(pairs)
