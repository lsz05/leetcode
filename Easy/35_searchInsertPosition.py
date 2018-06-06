def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        if target < nums[mid]:
            high = mid - 1
    return low
