def findMedianSortedArrays(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: float
    """
    m, n = len(A), len(B)
    # Ensure len(A) < len(B)
    if m > n:
        A, B, m, n = B, A, n, m

    """
    We divide the two lists into two parts respectively as

              left           |       right
    A[0], A[1], ... , A[i-1] | A[i], ... , A[m]
    B[0], B[1], ... , B[j-1] | B[j], ... , B[n]

    As long as we ensure
        (i)  len(left) == len(right)
        (ii) max(left) <= min(right)
          -- A[i-1] <= B[j]
          -- B[j-1] <= A[i]
    we will get the median.

    That is
        i + j == m - i + n - j (or m-i+n-j+1)
        max(A[i-1], B[j-1]) <= min(A[i], B[j])
    So j = (m + n + 1) / 2 - i

    Start binary search
        Initially set imin = 0, imax = m
        Set i = (imin + imax) / 2, we try to satisfy (ii) given (i) satisfied.
        <a> if (ii) is satisfied, stop searching.
        <b> if A[i-1] > B[j]： set imax = i-1 and search again
        <c> if B[j-1] > A[i]: set imin = i+1 and search again

    When the search is stopped, the median is
    -- max(A[i-1], B[j-1]) if m+n is odd
    -- (max(A[i-1], B[j-1]) + min(A[i], B[j])) / 2 if m+n is even

    """
    if n == 0:
        return ValueError
    imax, imin = m, 0
    while imin <= imax:
        i = (imax + imin) // 2
        j = (m + n + 1) // 2 - i
        print(i, j)
        if i > 0 and A[i - 1] > B[j]:  # <b>
            imax = i - 1
        elif i < m and B[j - 1] > A[i]:  # <c>
            imin = i + 1
        else:  # <a>
            if i == 0:
                left_max = B[j - 1]
            elif j == 0:
                left_max = A[i - 1]
            else:
                left_max = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return left_max
            else:
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                return (left_max + right_min) / 2.0
