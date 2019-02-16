"""
Queues
First/oldest element: head
Last/newest: Tail
add element to tail: enqueue
remove head element: dequeue
peek: look at head
Deque: double ended queue, generalized as a stack or a queue,
double linked
priority queue: assign each e;ement a priority, remove element
with the higher priority, if priority is same then the oldest element will be dequeued

cool library for queues: from collections import deque
"""
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        pass

    def peek(self):
        return self.storage[0]
        pass

    def dequeue(self):
        return self.storage.pop(0)
        pass

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()
