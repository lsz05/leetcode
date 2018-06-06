def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    if x > 0:
        y = int(str(x)[::-1])
    if x < 0:
        y = reverse(-x)
        y = -y
    if y >= 2147483647 or y <= -2147483647:
        return 0
    return y