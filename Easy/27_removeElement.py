def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = len(nums)
    for k in range(i, 0, -1):
        if nums[k - 1] == val:
            nums.pop(k - 1)
    return len(nums)