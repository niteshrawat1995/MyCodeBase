# Implementing singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        first_node = self.head
        new_node.next = first_node
        self.head = new_node

    def insert_after_node(self, prev_node_data, data):
        cur_node = self.head
        while cur_node.data != prev_node_data:
            cur_node = cur_node.next

        prev_node = cur_node

        if not prev_node:
            print('Previous node is not in the list!')
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    '''Similar to print function.'''

    def len_list(self):
        length = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            length += 1
        return length

    def swap_node(self, data1, data2):
        cur_node = self.head
        while cur_node:
            if cur_node.data == data1:
                first_node = cur_node
            if cur_node.data == data2:
                cur_node.data, first_node.data = first_node.data, cur_node.data
            cur_node = cur_node.next

    '''Reverse a linked list:
        A -> B -> C -> D -> None
     TO D -> C -> B -> A -> None or,
        A <- B <- C <- D   '''

    def reverse_list(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev

    '''Nth to the last node i.e
        A -> B -> C -> D -> None 2nd to the last node = C
        index(starting from 1) of second to the last = size - (n-1)'''

    def NthToLast(self, index):
        idx = 1
        size = self.len_list()
        index = size - (index - 1)
        cur_node = self.head
        while cur_node:
            if idx == index:
                return cur_node.data
            cur_node = cur_node.next
            idx += 1
    '''Rotating the linked list wrt pivot node .
       All nodes after pivot will move to the starting of the list and pivot will point to None.
       Hint: After rotation, intial last node will point to the intial first node. And new head will point to node next to pivot '''

    def rotate(self, pivot_data):
        cur_node = self.head
        # Storing the intial head node before rotation.
        p = cur_node

        while cur_node.next:
            if cur_node.data == pivot_data:
                pivot_node = cur_node
                # storing pivot next node(which will become first node after rotation.)
                new_first = cur_node.next
            cur_node = cur_node.next
        # Pointing last node to intial head node.
        cur_node.next = p
        # Pivot node pointing to None.
        pivot_node.next = None
        # Setting new head of the list after rotation
        self.head = new_first

        '''1
           3 6 5
           2 4 8
           ------
           6 1 3
            '''

    def sum_two_list(self, llist):
        grand_sum = []
        small_sum, carry = 0, 0
        cur_node1 = self.head
        cur_node2 = llist.head
        while cur_node1 or cur_node2:
            small_sum = cur_node1.data + cur_node2.data + carry
            if small_sum >= 10:
                carry = 1
                small_sum = small_sum % 10
            grand_sum.append(small_sum)
            cur_node1 = cur_node1.next
            cur_node2 = cur_node2.next
        return grand_sum[::-1]


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.prepend('E')
# llist.insert_after_node('B', 'F')
# llist.swap_node('A', 'B')
# llist.reverse_list()
# print(llist.NthToLast(3))
# llist.rotate('B')
# print(llist.last_node())
# llist.print_list()
# print(llist.len_list())

llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(llist1.sum_two_list(llist2))
