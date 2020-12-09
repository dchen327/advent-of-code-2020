nums = open('aoc9.txt').read().splitlines()
nums = list(map(int, nums))
# part 1
invalid_num = None
preamble_len = 5
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
        invalid_num = next_num
        break

print(invalid_num)
# part 2
l = 0
sum_ = 0
for r in range(len(nums)):
    sum_ += nums[r]
    while r - l >= 2 and sum_ > invalid_num:
        sum_ -= nums[l]
        l += 1
        if sum_ == invalid_num:
            x = nums[l:r+1]
            print(min(x) + max(x))
            break
