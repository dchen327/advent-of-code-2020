import numpy as np
from itertools import product

init_state = open('aoc17.txt').read().splitlines()
grid_size = 30
offset = grid_size // 2 - len(init_state) // 2
grid = np.zeros((grid_size, grid_size, grid_size))
for r in range(len(init_state)):
    for c in range(len(init_state[0])):
        grid[offset, r + offset, c + offset] = init_state[r][c] == '#'

max_radius = len(init_state) // 2 + 2
for _ in range(6):
    print(_ + 1)
    changes = []
    for r, c, h in product(range(grid_size // 2 - max_radius, grid_size // 2 + max_radius), repeat=3):
        num_active_neighbors = 0
        for i, j, k in product(range(-1, 2), repeat=3):
            # find neighbors
            if i == j == k == 0:  # skip self
                continue
            if all(0 <= pos < grid_size for pos in [r + i, c + j, h + k]):
                num_active_neighbors += grid[r + i, c + j, h + k]
        if grid[r, c, h] and num_active_neighbors not in [2, 3]:
            changes.append((r, c, h))
        elif not grid[r, c, h] and num_active_neighbors == 3:
            changes.append((r, c, h))
    for change in changes:
        grid[change] = 1 - grid[change]
    max_radius += 1

print(int(np.sum(grid)))

# part 2
grid = np.zeros((grid_size, grid_size, grid_size, grid_size))
for r in range(len(init_state)):
    for c in range(len(init_state[0])):
        grid[offset, offset, r + offset, c + offset] = init_state[r][c] == '#'

max_radius = len(init_state) // 2 + 2
for _ in range(6):
    print(_ + 1)
    changes = []
    new_grid = np.copy(grid)
    for r, c, h, t in product(range(grid_size // 2 - max_radius, grid_size // 2 + max_radius), repeat=4):
        num_active_neighbors = 0
        for i, j, k, l in product(range(-1, 2), repeat=4):
            # find neighbors
            if i == j == k == l == 0:  # skip self
                continue
            if all(0 <= pos < grid_size for pos in [r + i, c + j, h + k, t + l]):
                num_active_neighbors += grid[r + i, c + j, h + k, t + l]
        if grid[r, c, h, t] and num_active_neighbors not in [2, 3]:
            changes.append((r, c, h, t))
        if not grid[r, c, h, t] and num_active_neighbors == 3:
            changes.append((r, c, h, t))
    for change in changes:
        grid[change] = 1 - grid[change]
    max_radius += 1

print(int(np.sum(grid)))
