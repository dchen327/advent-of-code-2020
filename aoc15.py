from time import time
start = time()

start_nums = list(map(int, open('aoc15.txt').read().split(',')))
nums = [0] + start_nums[:]
turn_spoken = {num: i + 1 for i, num in enumerate(start_nums)}
for turn in range(len(start_nums), 3*10**7):
    last = nums[-1]
    if last in turn_spoken:
        nums.append(turn - turn_spoken[last])
    else:
        nums.append(0)
    turn_spoken[last] = turn


print(nums[2020])
print(nums[-1])
print(time() - start)
