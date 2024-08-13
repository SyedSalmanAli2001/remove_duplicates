nums = [2, 4, 12, 50, 50, 50, 90, 90]
#
# i = 0
# while i < len(nums) - 1:
#     if nums[i] == nums[i+1]:
#         nums.pop(i)
#     else:
#         i += 1
#
# print(nums)


def remove_duplicates(nums_array):
    i = 0
    while i < len(nums_array) - 1:
        if nums_array[i] == nums_array[i + 1]:
            nums_array.pop(i)
        else:
            i += 1
    return len(nums_array)


print(remove_duplicates(nums))
