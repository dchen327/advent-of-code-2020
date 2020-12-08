code = open('aoc8.txt').read().splitlines()
code = [line.split() for line in code]
# part 1
visited = set()
accumulator = 0
idx = 0
while idx not in visited:
    visited.add(idx)
    operation, argument = code[idx]
    if operation == 'acc':
        accumulator += int(argument)
        idx += 1
    elif operation == 'jmp':
        idx += int(argument)
    elif operation == 'nop':
        idx += 1

print(accumulator)

# part 2


def simulate(code):
    visited = set()
    accumulator = 0
    idx = 0
    while idx not in visited:
        if idx == len(code):  # code successfully terminated
            return accumulator
        visited.add(idx)
        operation, argument = code[idx]
        if operation == 'acc':
            accumulator += int(argument)
            idx += 1
        elif operation == 'jmp':
            idx += int(argument)
        elif operation == 'nop':
            idx += 1
    return None


# try all swaps
for i, line in enumerate(code):
    orig_op = code[i][0]
    if code[i][0] == 'nop':
        code[i][0] = 'jmp'
    elif code[i][0] == 'jmp':
        code[i][0] = 'nop'
    accumulator = simulate(code)
    if accumulator:
        print(accumulator)
        break
    code[i][0] = orig_op
