""" Assume list as a normal array. all element stored in contiguous memory location  """

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        self.queue = self.queue[1:]
        return data

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
queue.enqueue(5)
queue.delete()
print(queue.isempty())



