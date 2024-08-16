nums = []


def remove_duplicates(nums_arr):
    if not nums_arr:
        return 0

    j = 0
    for i in range(1, len(nums_arr)):
        if nums_arr[i] != nums_arr[j]:
            j += 1
            nums_arr[j] = nums_arr[i]
    return j + 1


unique_count = remove_duplicates(nums)
print(unique_count)
print(nums[:unique_count])

