lines = open('aoc14.txt').read().splitlines()
mem = [0] * 1000000


def apply_mask(val, mask):
    return ''.join(val[i] if mask[i] == 'X' else mask[i] for i in range(len(val)))


for line in lines:
    if line[:4] == 'mask':
        mask = line.split()[-1]
        continue
    idx, val = line[4:].split('] = ')  # ex) mem[5] = 12
    val = bin(int(val))[2:]
    val = apply_mask(val.zfill(36), mask)
    mem[int(idx)] = int(val, 2)

print(sum(mem))
