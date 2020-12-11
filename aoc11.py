# part 1
seats = open('aoc11.txt').read().splitlines()
seats = [list(row) for row in seats]
new_seats = [row[:] for row in seats]  # copy seats
while True:
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] not in 'L#':
                continue
            num_adj = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= r + i < len(seats) and 0 <= c + j < len(seats[0]):
                        num_adj += seats[r+i][c+j] == '#'
            if seats[r][c] == 'L' and num_adj == 0:  # empty, no adj
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and num_adj >= 4:
                new_seats[r][c] = 'L'
    if seats == new_seats:
        print(sum(row.count('#') for row in seats))
        break
    # print('\n'.join(''.join(row) for row in new_seats))
    seats = [row[:] for row in new_seats]

# part 2
seats = open('aoc11.txt').read().splitlines()
seats = [list(row) for row in seats]
new_seats = [row[:] for row in seats]  # copy seats
directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (-1, 1), (1, -1), (-1, -1)]
while True:
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] not in 'L#':
                continue
            num_visible = 0
            for i, j in directions:
                d = 1
                while 0 <= r + d * i < len(seats) and 0 <= c + d * j < len(seats[0]):
                    seat = seats[r+d*i][c+d*j]
                    if seat != '.':
                        num_visible += seat == '#'
                        break
                    d += 1

            if seats[r][c] == 'L' and num_visible == 0:  # empty, no adj
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and num_visible >= 5:
                new_seats[r][c] = 'L'
    if seats == new_seats:
        print(sum(row.count('#') for row in seats))
        break
    # print('\n'.join(''.join(row) for row in new_seats))
    # print()
    seats = [row[:] for row in new_seats]
