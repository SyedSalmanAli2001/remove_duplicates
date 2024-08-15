
#
# i = 0
# while i < len(nums) - 1:
#     if nums[i] == nums[i+1]:
#         nums.pop(i)
#     else:
#         i += 1
#
# print(nums)


# def remove_duplicates(nums_array):
#     i = 0
#     while i < len(nums_array) - 1:
#         if nums_array[i] == nums_array[i + 1]:
#             nums_array.pop(i)
#         else:
#             i += 1
#     return len(nums_array)
#
#
# print(remove_duplicates(nums))

nums = [2, 4, 12, 50, 50, 50, 90, 90, 91, 91, 2]
# given array is already sorted


def remove_duplicates(nums_arr):
    j = 0
    for i in range(1, len(nums_arr)):
        if nums_arr[i] != nums_arr[j]:
            j += 1
            nums_arr[j] = nums_arr[i]
    return j + 1


unique_count = remove_duplicates(nums)
print(unique_count)
print(nums[:unique_count])

