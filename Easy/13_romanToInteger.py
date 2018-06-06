def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0

    # M=1000
    # D=500
    # C=100
    # L=50
    # X=10
    # V=5
    # I=1

    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    while i < len(s):
        if i + 1 < len(s) and dict[s[i]] < dict[s[i + 1]]:
            result = result + dict[s[i + 1]] - dict[s[i]]
            i = i + 2
        else:
            result = result + dict[s[i]]
            i = i + 1
    return result
