def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums), 1, -1):
        if nums[i - 1] == nums[i - 2]:
            nums.pop(i - 1)
    return len(nums)