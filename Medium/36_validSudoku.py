import collections

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = board
    cols = [[rows[j][i] for j in range(9)] for i in range(9)]
    subs = []

    new_subs = []
    for m in range(3):
        sub = board[3 * m: 3 * m + 3]
        for n in range(3):
            new_subs.append([row[3 * n: 3 * n + 3] for row in sub])
    for sub in new_subs:
        subs.append(sub[0] + sub[1] + sub[2])
    for ele in rows + cols + subs:
        counter = dict(collections.Counter(ele))
        if '.' in counter:
            del counter['.']
        if counter and max(counter.values()) > 1:
            return False
    return True