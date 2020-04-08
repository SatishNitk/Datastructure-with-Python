class node:
    def __init__(self, data = None):
        self.data = data
        self.next = self
        self.prev = self


class Circular_linked_list:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node  = node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = self.head 

    def display(self):
        curr = self.head
        ele = []
        while curr.next != self.head:
            ele.append(curr.data)
            curr = curr.next
        ele.append(curr.data)
        print(ele)

    def length(self):
        curr = self.head
        counter = 0
        while curr.next != self.head:
            curr = curr.next
            counter += 1
        counter += 1
        return counter



circular_linked_list = Circular_linked_list()
circular_linked_list.append(3)
circular_linked_list.append(4)
circular_linked_list.append(332)
circular_linked_list.append(33)
circular_linked_list.append(332)

circular_linked_list.display()
print("Length:- ",circular_linked_list.length())


