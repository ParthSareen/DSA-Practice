# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        tail = dummy

        while head:
            first = head
            second = head.next
            head = head.next.next if head.next else None

            if second:
                tail.next = second
                tail = tail.next
            tail.next = first
            tail = tail.next

        tail.next = None

        return dummy.next
