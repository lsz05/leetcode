def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0

    def DFS(grid, i, j):
        if i < 0 or i > row - 1 or j < 0 or j > col - 1 or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
            DFS(grid, i - 1, j)
            DFS(grid, i + 1, j)
            DFS(grid, i, j - 1)
            DFS(grid, i, j + 1)

    res = 0
    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                DFS(grid, i, j)
                res += 1
    return res