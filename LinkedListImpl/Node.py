class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def print_node(self):
        print(str(self.data)+" -> ", end=" ")



