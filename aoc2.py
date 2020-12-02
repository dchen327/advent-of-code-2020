# part 1
f = 'ao2.txt'
num_valid = 0
for line in open(f).read().splitlines():
    policy, pw = line.split(': ')
    count_range, letter = policy.split()
    low, high = map(int, count_range.split('-'))
    count = pw.count(letter)
    num_valid += low <= count <= high
print(num_valid)

# part 2
num_valid = 0
for line in open(f).read().splitlines():
    policy, pw = line.split(': ')
    count_range, letter = policy.split()
    idx1, idx2 = map(int, count_range.split('-'))
    num_valid += (pw[idx1 - 1] == letter) ^ (pw[idx2 - 1] == letter)

print(num_valid)
