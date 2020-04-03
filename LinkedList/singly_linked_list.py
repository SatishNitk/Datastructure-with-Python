class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = node()
        self.head_clone = node()

    def append(self, data):
        new_node  = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        counter = 0
        while curr.next != None:
            counter += 1
            curr = curr.next
        return counter

    def display(self):
        ele = []
        curr= self.head
        while  curr.next != None:
            curr = curr.next
            ele.append(curr.data)
        print(ele)

    def search(self, data):
        curr = self.head.next
        index = 0
        while curr != None:
            if(curr.data == data):
                return "Found at index %s"%(index)
            index += 1
            curr = curr.next
        return "Not found"

    def find_middle(self):
        curr = self.head.next; slow = curr; fast = curr
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def reverse(self):
        curr = self.head.next; next = None; prev = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head.next = prev

    def clone_linked_list(self):
        curr = self.head.next
        curr_clone = node()
        temp_curr_clone  = curr_clone
        while  curr != None:
            new_node = node(curr.data)
            if curr_clone.next == None:
                curr_clone.next = new_node
            else:
                while curr_clone.next != None:
                    curr_clone = curr_clone.next
                curr_clone.next = new_node
            curr = curr.next

        while  temp_curr_clone.next != None:
            temp_curr_clone = temp_curr_clone.next
            print(temp_curr_clone.data, end=' ')
        print("\n")

    def delete_element(self, index):
        if self.length() < index:
            print("index does not exists")
        elif index == 1:
            self.head.next = self.head.next.next
        else:
            curr = self.head.next
            counter = 1
            while counter != index-1:
                counter+=1
                curr = curr.next
            curr.next = curr.next.next


    def insert_element(self, index, data):
        new_node = node(data)
        if self.length() + 1<= index:
            print("index does not exists")
        elif index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            curr = self.head.next
            counter = 0
            while counter != index-1:
                counter +=1 
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node





link_list = Linked_list()
link_list.display()
link_list.append(3)
link_list.append(13)
link_list.append(23)
link_list.append(233)
link_list.append(2323)
link_list.append(2332)
link_list.append(23327)
print("Linekd list")
link_list.display()
print("search in linked list")
print(link_list.search(23))
print("Middle element in a linked list")
print(link_list.find_middle())
print("reverse of link_list")
link_list.reverse() 
link_list.display()
print("CLone of linked list")
link_list.clone_linked_list()
print("delete element")
link_list.delete_element(3)    
link_list.display()
print("inser element")
link_list.insert_element(3,43)
link_list.display()
