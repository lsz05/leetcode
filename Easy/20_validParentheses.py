def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    left = ["(", "[", "{"]
    right = [")", "]", "}"]

    for i in s:
        if i in left:
            stack.append(i)
        if i in right:
            if not stack:
                return False
            if len(stack) < 1:
                return False
            top = stack[len(stack) - 1]
            if top not in left:
                return False
            if top in left and left.index(top) != right.index(i):
                return False
            stack.pop(-1)
    if not stack:
        return True
    else:
        return False