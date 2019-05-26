# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = None
        p2 = head
        
        while p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        
        return p1