nums = open('aoc9.txt').read().splitlines()
nums = list(map(int, nums))
preamble_len = 25
for start_idx in range(len(nums) - preamble_len):
    a = nums[start_idx:start_idx + preamble_len]
    next_num = nums[start_idx + preamble_len]
    valid = False
    for i in range(preamble_len):
        for j in range(i + 1, preamble_len):
            if a[i] + a[j] == next_num:
                valid = True
                break
    if not valid:
        print(next_num)
        break
