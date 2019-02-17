# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        array = l1.append(l2)
        less = []
        equal = []
        greater = []
        n = len(array)//2
        if len(array) > 1:
            pivot = array[n]

            for i in array:
                if i < pivot:
                    less.append(i)
                elif i == pivot:
                    equal.append(i)
                elif i > pivot:
                    greater.append(i)
            return quicksort(less) + equal + quicksort(greater)
        else:
            return array
obj = Solution()
obj.mergeTwoLists([])
