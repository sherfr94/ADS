from LinkedListImpl.Node import Node

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, data):
        self.size += 1
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def remove(self, data):
        curr = self.head
        if curr is not None:
            #case remove 1st Node
            if curr.data == data:
                self.head = curr.next
                self.size -= 1
            #case remove other Node
            else:
                while curr.next is not None:
                    prev = curr
                    curr = curr.next
                    if curr.data == data:
                        prev.next = curr.next
                        self.size -= 1
                        return

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            curr.print_node()
            curr = curr.next
        print("") #new line after linkedlist was printed
