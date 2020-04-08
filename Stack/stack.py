class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        self.stack = self.stack[:len(self.stack)-1]
        return data

    def size(self):
        return len(self.stack)


    def peek(self):
        return self.stack[-1]

    def delete(self):
        self.stack.clear()

    def display(self):
        print(self.stack)

    def isEmpty(self):
        return False if len(self.stack) else True

stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.display()
print(stack.isEmpty())
stack.pop()
stack.pop()
stack.display()
stack.push(43)
print(stack.peek())
stack.delete()
print(stack.isEmpty())
stack.display()



