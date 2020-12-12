instructions = open('aoc12.txt').read().splitlines()
print(instructions)
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

print(x, y)
