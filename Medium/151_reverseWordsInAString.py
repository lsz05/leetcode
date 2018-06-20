def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return " ".join(s.strip().split()[::-1])