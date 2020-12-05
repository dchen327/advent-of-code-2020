for seat in open('aoc5.txt').read().splitlines():
    row, col = seat[:7], seat[7:]
    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('L', '0').replace('R', '1')
    row = int(row, 2)  # convert from binary to dec
    col = int(col, 2)
    print(row, col)
