instructions = open('aoc12.txt').read().splitlines()
# part 1
x, y = 0, 0
facing = 'E'
dir_to_pos = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
directions = 'NESW'
for instruction in instructions:
    action, value = instruction[0], int(instruction[1:])
    if action in 'NESWF':
        if action == 'F':
            action = facing
        dx, dy = dir_to_pos[action]
        x += value * dx
        y += value * dy
    elif action in 'LR':
        if action == 'L':
            action = 'R'
            value = 360 - value  # convert all to right, or clockwise
        curr_idx = directions.index(facing)
        shift = (value // 90)
        new_idx = (curr_idx + shift) % 4
        facing = directions[new_idx]

print(abs(x) + abs(y))

# part 2
x, y = 0, 0  # ship pos
wx, wy = 10, 1  # waypoint pos

dir_to_pos = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
for instruction in instructions:
    action, value = instruction[0], int(instruction[1:])
    if action in 'NESW':
        dx, dy = dir_to_pos[action]
        wx += value * dx
        wy += value * dy
    elif action == 'F':
        x += value * wx
        y += value * wy
    elif action in 'LR':
        if action == 'L':
            action = 'R'
            value = 360 - value  # convert all to right, or clockwise
        num_rotations = (value // 90) % 4  # num 90 deg rotations
        for _ in range(num_rotations):
            wx, wy = wy, -wx  # rotate 90 degrees

print(abs(x) + abs(y))
