# Implementing doubly linked list:
class Node(object):
    """Node will have data ,prev and next"""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList(object):
    """Linked list will have head attribute."""

    def __init__(self):
        self.head = None

    def append(self, data):
        # create new node:
        new_node = Node(data)
        # check if linked list is empty:
        if self.head is None:
            self.head = new_node.prev
            return
        while self.head.next != None:
            self.head = self.head.next
        self.head.next = new_node.prev
        new_node.prev = self.head

    def print_list(self):
        while self.head != None:
            print(str(self.head.data))
            self.head = self.head.next


dll = LinkedList()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')

dll.print_list()
