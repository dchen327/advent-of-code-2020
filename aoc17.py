import numpy as np
from itertools import product

init_state = open('aoc17.txt').read().splitlines()
grid_size = 30
offset = grid_size // 2 - len(init_state) // 2
grid = np.zeros((grid_size, grid_size, grid_size))
for r in range(len(init_state)):
    for c in range(len(init_state[0])):
        grid[offset, r + offset, c + offset] = init_state[r][c] == '#'

for _ in range(6):
    new_grid = np.copy(grid)
    for r, c, h in product(range(grid_size), repeat=3):
        num_active_neighbors = 0
        for i, j, k in product(range(-1, 2), repeat=3):
            # find neighbors
            if i == j == k == 0:
                continue
            if all(0 <= pos < grid_size for pos in [r + i, c + j, h + k]):
                num_active_neighbors += grid[r + i, c + j, h + k]
        if grid[r, c, h] and num_active_neighbors not in [2, 3]:
            new_grid[r, c, h] = 0
        if not grid[r, c, h] and num_active_neighbors == 3:
            new_grid[r, c, h] = 1
    grid = new_grid

print(int(np.sum(grid)))
