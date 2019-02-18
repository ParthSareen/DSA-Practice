# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()

            if top != slow.val:
                return False
            slow = slow.next
        return True

            
