from LinkedListImpl.Node import Node
from LinkedListImpl.LinkedList import LinkedList

if __name__ == '__main__':

    print("====================")
    print("TEST NODE")
    node1 = Node(1)
    node2 = Node(2)
    print(node1.data)
    print(node1.next)
    node1.print_node()
    print()
    print("====================")

    print("TEST INSERT LINKED LIST")
    linkedlist1 = LinkedList()
    linkedlist1.insert(1)
    linkedlist1.insert(2)
    linkedlist1.insert(3)
    linkedlist1.insert(4)

    linkedlist1.print_linked_list()
    print('size:', linkedlist1.size)
    print("====================")

    print("TEST REMOVE LINKED LIST")
    linkedlist1 = LinkedList()
    linkedlist1.insert(1)
    linkedlist1.insert(2)
    linkedlist1.remove(1)
    linkedlist1.insert(4)

    linkedlist1.print_linked_list()
    print('size:', linkedlist1.size)
    print("====================")

