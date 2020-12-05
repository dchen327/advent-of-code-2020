max_id = 0
for seat in open('aoc5.txt').read().splitlines():
    # convert to binary
    seat = seat.replace('F', '0').replace(
        'B', '1').replace('L', '0').replace('R', '1')
    max_id = max(max_id, int(seat, 2))

print(max_id)
