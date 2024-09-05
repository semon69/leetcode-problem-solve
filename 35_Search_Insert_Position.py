def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right -left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
    # for i in range(len(nums)):
    #     if nums[i] >= target:
    #         return i
    # return len(nums)

print(searchInsert([1,3,5,6], 2))
