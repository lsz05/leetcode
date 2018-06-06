def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    i = 0
    while i <= len(haystack) - len(needle):
        j = 0
        while j < len(needle):
            if haystack[i + j] != needle[j]:
                break
            else:
                j += 1
            if j == len(needle):
                return i
        i += 1
    return -1