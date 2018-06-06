# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def toList(l):
        L = []
        while l:
            L.append(l.val)
            l = l.next
        return L
    def toNode(L):
        if len(L) == 1:
            return ListNode(L[0])
        else:
            l = ListNode(L[0])
            l.next = toNode(L[1:])
            return l
    L1, L2 = toList(l1), toList(l2)
    print(L1, L2)
    if len(L2) > len(L1):
        L = L1
        L1 = L2
        L2 = L
    for i in range(len(L2), len(L1)):
        L2.append(0)
    L = []
    flag = 0
    for i in range(len(L1)):
        tmp = L1[i] + L2[i] + flag
        if tmp > 9:
            tmp = tmp - 10
            flag = 1
        else:
            flag = 0
        L.append(tmp)
    if flag == 1:
        L.append(1)
    return toNode(L)