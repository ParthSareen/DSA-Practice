# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        dummy1 = dummy2 = ListNode(0)
        #dummy1,dummy2 = l1, l2
        print(l1.val)
        while l1 and l2:
            if l1.val < l2.val:
                curr_low = l1
                l1 = l1.next
            else:
                curr_low = l2
                l2 = l2.next

            dummy2.next = curr_low
            dummy2 = dummy2.next
        dummy2.next = l1 or l2
        return dummy1.next
