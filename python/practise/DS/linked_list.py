# Implementing singly linked list.

class Node:
    def __init__(self,data):        
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head=new_node
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node !=None:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self,data):
        new_node = Node(data)
        # When linked listis empty.
        if self.head == None:
            self.head= new_node
            return
        
        #first_node = self.head
        
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node_data,data):
        cur_node = self.head
        while cur_node.data != prev_node_data:
            cur_node = cur_node.next
            
        prev_node = cur_node

        if not prev_node:
            print('Previous node is not in the list!')
            return
        
        new_node = Node(data)

        new_node.next =prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
        cur_node = self.head
        #Checking whether linked list is empty.
        if cur_node ==None:
            print('Linked list is Empty!')
            return
        
        #key present in the first position.
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        #key present at any position.
        #Need to track the previous node as well.
        prev_node = None
        while cur_node.data !=key:
            prev=cur_node
            cur_node = cur_node.next
        prev.next = cur_node.next
        cur_node = None
        return       
    

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.prepend('E')
llist.insert_after_node('B','F')
#llist.delete_node('E')
#llist.delete_node('A')
llist.print_list()
