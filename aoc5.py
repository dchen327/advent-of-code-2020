seats = open('aoc5.txt').read().splitlines()
ids = []
# part 1
max_id = 0
for seat in seats:
    # convert to binary
    seat = seat.replace('F', '0').replace(
        'B', '1').replace('L', '0').replace('R', '1')
    id_ = int(seat, 2)
    max_id = max(max_id, id_)
    ids.append(id_)

print(max_id)

# part 2
ids.sort()
for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] == 2:
        print(ids[i] + 1)
        break
