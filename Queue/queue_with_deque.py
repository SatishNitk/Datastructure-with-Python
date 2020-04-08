""" Internally deque has implemented using doubly linked list. so there is no any contiguous memory allocation"""
from collections import deque
class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop()

    def delete(self):
        self.queue.clear()

    def peek(self):
        return self.queue[0]

    def display(self):
        print(self.queue)

    def isempty(self):
        return False if len(self.queue) else True



queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
queue.dequeue()
queue.dequeue()
print(queue.isempty())
queue.display()
queue.dequeue()
print(queue.isempty())
queue.enqueue(51)
queue.enqueue(512)
print(queue.peek())
queue.display()
queue.delete()
print(queue.isempty())



