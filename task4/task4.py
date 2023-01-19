import sys


with open(sys.argv[1], 'r') as file:
    nums = [int(line) for line in file]

median = sum(nums) // len(nums)
count = 0
for elm in nums:
    if elm != median:
        count += abs(elm - median)

print(count)
