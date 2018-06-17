# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 1. Cut the list into two halves
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        # Part 1: head ~ pre
        # Part 2: slow ~

        # 2. Sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # 3. Merge two halves
        return self.merge(l1, l2)

    def merge(self, left, right):
        p = ListNode(0)
        new = p
        while left and right:
            if left.val <= right.val:
                new.next = left
                left = left.next
            else:
                new.next = right
                right = right.next
            new = new.next
        if not left:
            new.next = right
        if not right:
            new.next = left
        return p.next
