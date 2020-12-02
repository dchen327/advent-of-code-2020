f = 'ao2.txt'
num_valid = 0
for line in open(f).read().splitlines():
    policy, pw = line.split(': ')
    count_range, letter = policy.split()
    low, high = map(int, count_range.split('-'))
    count = pw.count(letter)
    num_valid += low <= count <= high
print(num_valid)
