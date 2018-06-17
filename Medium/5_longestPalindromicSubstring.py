class Solution:
    def __init__(self):
        self.l, self.maxLen = 0, 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for m in range(len(s)):
            self.extendPalindrome(s, m, m)
            self.extendPalindrome(s, m, m+1)
        return s[self.l:self.l+self.maxLen]
    def extendPalindrome(self, s, i, j):
        while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
            i -= 1
            j += 1
        if self.maxLen < j-i-1:
            self.maxLen = j-i-1
            self.l = i+1