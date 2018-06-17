# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import queue
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = ListNode(0)
        new = p
        q = PriorityQueue()
        for i in range(len(lists)):
            if lists[i]:
                q.put((lists[i].val, i, lists[i]))
        while q.qsize() > 0:
            node = q.get()
            new.next, idx = node[-1], node[1]
            new = new.next
            if new.next:
                q.put((new.next.val, idx, new.next))
        return p.next
