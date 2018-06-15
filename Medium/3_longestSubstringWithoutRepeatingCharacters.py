def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    used = {}
    start = maxLen = 0
    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            maxLen = max(maxLen, i - start + 1)
        used[s[i]] = i
    return maxLen