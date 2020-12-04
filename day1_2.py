nums = []

with open('day1_1_input.txt', 'r') as f:
    for line in f:
        nums.append(int(line))

def solveFor2(nums, i):
    map_ = {}
    target = 2020 - nums[i];
    for j in range(len(nums)):
        if (i == j):
            continue
        n = nums[j]
        remainder = target - n
        if str(n) in map_:
            print(map_[str(n)]*n*nums[i])
        else:
            map_[str(remainder)] = n

for i in range(len(nums)):
    solveFor2(nums, i)
