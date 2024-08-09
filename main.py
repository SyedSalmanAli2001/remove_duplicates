nums = [2, 4, 12, 50, 50, 50, 90, 90]

for i in range(len(nums)-1):
    if nums[i+1] == nums[i]:
        nums.remove(nums[i])

print(nums)