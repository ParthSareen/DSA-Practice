# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        runner = dummy
        current = dummy

        for i in range(0,n+1):
            if runner is None:
                return None
            runner = runner.next

        while runner is not None:
            current = current.next
            runner = runner.next

        current.next = current.next.next
        return dummy.next
