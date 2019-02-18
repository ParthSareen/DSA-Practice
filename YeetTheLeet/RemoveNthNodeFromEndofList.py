# Definition for singly-linked list.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = Node()

    def length(self):
        cur = self.head # change to head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        erase = self.length() - n
        cur_index = 0
        cur_node = self.head #change to head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == erase:
                last_node.next = cur_node.next
                return #self.head
            cur_index += 1

list = Solution()
a=list.append(1)
list.append(2)
list.append(4)
print(list.length())
list.display()
print(list.removeNthFromEnd(a,2))
list.display()
