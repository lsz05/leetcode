def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if not s:
        return ""
    if numRows == 1:
        return s
    ret = []
    for i in range(numRows):
        ret.append([])
    for i in range(len(s)):
        if i % (2 * numRows - 2) <= numRows - 1:
            ret[i % (2 * numRows - 2)].append(s[i])
        else:
            ret[-i % (2 * numRows - 2)].append(s[i])
    j = str()
    for i in ret:
        i = ''.join(i)
        print(i)
        j = j + i
    return j