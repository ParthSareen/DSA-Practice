#linkedLists.py
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None #default value
		self.prev = None

def count_nodes(head):
	#head != null/none
	count = 1
	current = head
	while current.next is not None:
		current = current.next
		count += 1
	return count

class linkedList:
	def __init__(self):
		self.headVal = None

	def traverse(self):
		printVal = self.headVal
		while printVal is not None:
			print (printVal.data)
			printVal = printVal.next

	def newI(self, newData):
		NewNode = Node(newData)

		NewNode.next= self.headVal
		self.headVal = NewNode

	def newF(self, newData):
		NewNode = Node(newData)
		if self.headVal is None:
			self.headVal = NewNode
			return
		laste = self.headVal
		while(laste.next):
			laste = laste.next
		laste.next = NewNode
		else:
			self.head = NewNode

	def between(self, middle_node, newData):
		if middle_node is None:
			print("The mentioned node is null")
			return

	def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

		NewNode = Node(newData)
		NewNode.next = middle_node.next
		middle_node.next = NewNode

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
print("The list's length is ")
print(count_nodes(nodeA))
####################################
list1 = linkedList()
list1.headVal = Node(5)
e2 = Node(2)
e3 = Node(9)
#first to second link
list1.headVal.next = e2
#second to third link
e2.next = e3
print(".\n")
list1.between(list1.headVal, "hi")
list1.newI(1)
list1.newF(7)
list1.traverse()
