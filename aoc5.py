for seat in open('aoc5.txt').read().splitlines():
    seat = seat.replace('F', '0').replace(
        'B', '1').replace('L', '0').replace('R', '1')
    print(int(seat, 2))
