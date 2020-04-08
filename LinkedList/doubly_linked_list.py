class node:

    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoubliLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if(self.head == None):
            self.head = new_node
        else:
            curr = self.head 
            while(curr.next != None):
                curr = curr.next
            new_node.prev = curr
            curr.next = new_node

    def display(self, head = None):
        curr = head if head else self.head
        element = []
        while curr != None:
            element.append(curr.data)
            curr = curr.next
        print("element: = %s" %element)

    def length(self):
        curr = self.head
        counter = 0
        while  curr:
            counter += 1
            curr = curr.next
        return counter


    def find_mid(self):
        curr = self.head
        slow = self.head
        fast = self.head
        # while(slow and fast and fast.next and fast.next.next):  it can be used for prev element if no of ele is even
        while(slow and fast  and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head = None):
        curr = head if head else self.head
        prev = None
        while curr != None:
            next_element = curr.next
            curr.next = prev
            prev = curr
            curr = next_element
        return prev

    def check_for_palindrome(self):
        curr = self.head
        flag = True
        mid_object = self.find_mid()
        after_reverse = self.reverse_list(mid_object)
        while after_reverse != None:
            if after_reverse.data != curr.data:
                flag = False
                break
            after_reverse = after_reverse.next
            curr = curr.next
        return True if flag else False

    def swap_kth_node_from_beg_and_fom_end(self, kth):
        if self.length() < kth:
            print("Not possible to exchange, bcz no more element")
            return
        curr = self.head
        index = 1 
        while  index != kth:
            curr = curr.next
            index += 1

        from_beg = curr
        from_end = self.head
        to_check = curr

        while  to_check.next:
            from_end = from_end.next
            to_check = to_check.next
            
        from_beg.prev.next = from_end
        from_beg.next.prev = from_end
        from_end.prev.next = from_beg
        from_end.next.prev = from_beg
        t  = from_beg.prev
        from_beg.prev = from_end.prev
        from_end.prev = t
        t = from_beg.next
        from_beg.next = from_end.next
        from_end.next = t






doublylinkedlist  = DoubliLinkedList()
doublylinkedlist.append(1)
doublylinkedlist.append(2)
doublylinkedlist.append(3)
doublylinkedlist.append(4)
doublylinkedlist.append(5)

doublylinkedlist.display()
doublylinkedlist.swap_kth_node_from_beg_and_fom_end(4)
doublylinkedlist.display()

print("mid element %s "% doublylinkedlist.find_mid().data)
print("\nreverse_list", end  = ' ')
doublylinkedlist.display(doublylinkedlist.reverse_list())
print("Palindrome status :- ",doublylinkedlist.check_for_palindrome())




