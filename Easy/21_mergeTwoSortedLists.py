# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    res = []
    while l1 and l2:
        if l1.val <= l2.val:
            res.append(l1.val)
            l1 = l1.next
        else:
            res.append(l2.val)
            l2 = l2.next
    while l1:
        res.append(l1.val)
        l1 = l1.next
    while l2:
        res.append(l2.val)
        l2 = l2.next
    return res