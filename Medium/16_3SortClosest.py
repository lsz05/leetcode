def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum
            if abs(result - target) > abs(sum - target):
                result = sum
            if sum > target:
                k -= 1
            if sum < target:
                j += 1
    return result