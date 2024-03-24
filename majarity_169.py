def majorityElement(nums):
    newArray = sorted(nums)
    middle_index = len(newArray) // 2
    return newArray[middle_index]

print(majorityElement([2,2,1,1,1,2,2]))