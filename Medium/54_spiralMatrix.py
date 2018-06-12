def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return []
    if len(matrix) == 1:
        return matrix[0]
    if len(matrix[0]) == 1:
        return [row[0] for row in matrix]
    res = []

    def isEmpty(matrix):
        if not matrix:
            return True
        if len(matrix[0]) == 0:
            return True
        return False

    while True:
        for i in range(len(matrix[0])):
            res.append(matrix[0][i])
        matrix = matrix[1:]
        print(matrix)
        if isEmpty(matrix) == True:
            return res
        for i in range(len(matrix)):
            res.append(matrix[i][-1])
        matrix = [row[:-1] for row in matrix]
        print(matrix)
        if isEmpty(matrix) == True:
            return res
        for i in range(len(matrix[0]) - 1, -1, -1):
            res.append(matrix[-1][i])
        matrix = matrix[:-1]
        print(matrix)
        if isEmpty(matrix) == True:
            return res
        for i in range(len(matrix) - 1, -1, -1):
            res.append(matrix[i][0])
        matrix = [row[1:] for row in matrix]
        print(matrix)

        # print(matrix)
        if isEmpty(matrix) == True:
            return res