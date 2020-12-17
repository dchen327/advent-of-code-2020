import numpy as np
from itertools import product

init_state = open('aoc17.txt').read().splitlines()
grid_size = 15
offset = grid_size // 2 - len(init_state) // 2
grid = np.zeros((grid_size, grid_size, grid_size))
for r in range(len(init_state)):
    for c in range(len(init_state[0])):
        grid[offset, r + offset, c + offset] = init_state[r][c] == '#'

for _ in range(6):
    print(_ + 1)
    for r, c, h in product(range(grid_size), repeat=3):
        num_active_neighbors = 0
        for i, j, k in product(range(-1, 2), repeat=3):
            # find neighbors
            if i == j == k == 0:  # skip self
                continue
            if all(0 <= pos < grid_size for pos in [r + i, c + j, h + k]):
                num_active_neighbors += grid[r + i, c + j, h + k]
        if grid[r, c, h] and num_active_neighbors not in [2, 3]:
            new_grid[r, c, h] = 0
        if not grid[r, c, h] and num_active_neighbors == 3:
            new_grid[r, c, h] = 1
    grid = new_grid

print(int(np.sum(grid)))

# part 2
grid = np.zeros((grid_size, grid_size, grid_size, grid_size))
for r in range(len(init_state)):
    for c in range(len(init_state[0])):
        grid[offset, offset, r + offset, c + offset] = init_state[r][c] == '#'

quit()
for _ in range(6):
    print(_ + 1)
    new_grid = np.copy(grid)
    for r, c, h, t in product(range(grid_size), repeat=4):
        num_active_neighbors = 0
        for i, j, k, l in product(range(-1, 2), repeat=4):
            # find neighbors
            if i == j == k == l == 0:  # skip self
                continue
            if all(0 <= pos < grid_size for pos in [r + i, c + j, h + k, t + l]):
                num_active_neighbors += grid[r + i, c + j, h + k, t + l]
        if grid[r, c, h, t] and num_active_neighbors not in [2, 3]:
            new_grid[r, c, h, t] = 0
        if not grid[r, c, h, t] and num_active_neighbors == 3:
            new_grid[r, c, h, t] = 1
    grid = new_grid

print(int(np.sum(grid)))
