#  Implementing Queue using
#1. python list.
#2. linked list in python 

'''queue = [1,2,3,4,5,6]

def enqueue(seq,data):
    seq.insert(0,data)
    return ''.join(str(seq))

def dequeue(seq):
    seq.pop()
    return ''.join(str(seq))

queue = [1,2,3,4,5,6]

print(enqueue(queue,10))
print(dequeue(queue))'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head =None

    def print_list(self):
        cur_node = self.head
        while cur_node !=None:
            print(cur_node.data)
            cur_node = cur_node.next    

    def enqueue(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head    
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        

    def dequeue(self):
        cur_node = self.head
        self.head = cur_node.next
        cur_node = None
        
        
llist = LinkedList()
llist.enqueue('A')
llist.enqueue('B')
llist.enqueue('C')
llist.enqueue('D')
llist.dequeue()
llist.print_list()




        
        


    
