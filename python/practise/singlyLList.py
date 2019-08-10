# singly linked list:


class Node(object):
    """used to create a node with data and a pointer to the next node."""

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList(object):
    """Linked list class with head attribute and size and various LL operations."""

    def __init__(self):
        self.head = None
        self.size = 0
        self.idx = 0

    # insertion at the end
    def append(self, data):
        new_node = Node(data)
        curr_node = self.head
        # check whether node is empty or not.
        if curr_node is None:
            self.head = new_node
            self.size += 1
            return
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.size += 1

    # insertion at the start:
    def prepend(self, data):
        new_node = Node(data)
        curr_node = self.head  # curr_node is the first node right now.
        # check whether the list is empty or not(i.e head points to None)
        if curr_node is None:
            self.head = new_node
            self.size += 1
            return
        new_node.next = curr_node  # new_node next point to first node.
        self.head = new_node  # head point to new_node.
        self.size += 1

    # insertion at specific point:
    def insert_node(self, data, index):
        new_node = Node(data)
        curr_node = self.head  # curr_node is the first node right now.

        if curr_node is None:  # if the list is empty.
            self.head = new_node
        while curr_node.next != None:
            curr_node = curr_node.next
            self.idx += 1

            if index == int(self.idx):
                new_node.next = curr_node.next
                curr_node.next = new_node
                self.size += 1
                print('Got it')
    # Printing the linked list:

    def print_list(self):
        curr_node = self.head
        while curr_node != None:
            print(str(curr_node.data))
            curr_node = curr_node.next


llist = LinkedList()


llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.prepend('E')
llist.insert_node('Z', 2)
llist.print_list()
print(llist.size)
