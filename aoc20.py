lines = open('aoc20.txt').read().splitlines()
N = len(lines[1])
tiles = {}
for i in range(0, len(lines), N + 2):
    tile_info = lines[i:i+12]
    tile_id = int(tile_info[0].rstrip(':').split()[-1])
    tile = tile_info[1:]
    tiles[tile_id] = tile
