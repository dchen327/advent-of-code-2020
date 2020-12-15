from itertools import product

lines = open('aoc14.txt').read().splitlines()
mem = {}


def apply_mask(val, mask):
    return ''.join(val[i] if mask[i] == 'X' else mask[i] for i in range(len(val)))


mask = ''
for line in lines:
    if line[:4] == 'mask':
        mask = line.split()[-1]
        continue
    idx, val = line[4:].split('] = ')  # ex) mem[5] = 12
    val = bin(int(val))[2:]
    val = apply_mask(val.zfill(36), mask)
    mem[int(idx)] = int(val, 2)

print(sum(mem.values()))

mem = {}


def apply_mask2(val, mask):
    return ''.join(val[i] if mask[i] == '0' else mask[i] for i in range(len(val)))


for line in lines:
    if line[:4] == 'mask':
        mask = line.split()[-1]
        continue
    addr, val = map(int, line[4:].split('] = '))  # ex) mem[5] = 12
    addr = bin(addr)[2:].zfill(36)
    addr = apply_mask2(addr, mask)
    num_X = addr.count('X')
    X_idx = [i for i, j in enumerate(addr) if j == 'X']
    for t in product('01', repeat=num_X):
        new_addr = list(addr)
        for i, j in enumerate(X_idx):
            new_addr[j] = t[i]
        new_addr = int(''.join(new_addr), 2)
        mem[new_addr] = val

print(sum(mem.values()))
