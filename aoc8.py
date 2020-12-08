code = open('aoc8.txt').read().splitlines()
code = [line.split() for line in code]
visited = set()
accumulator = 0
idx = 0
while idx not in visited:
    visited.add(idx)
    operation, argument = code[idx]
    if operation == 'nop':
        idx += 1
    elif operation == 'acc':
        accumulator += int(argument)
        idx += 1
    elif operation == 'jmp':
        idx += int(argument)

print(accumulator)
