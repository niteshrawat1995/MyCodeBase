'''
STACK data structure
'''


class Stack(object):
    """implementing stack operations"""

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek():
        if not self.is_empty():
            return self.items[-1]
        return None

    def get_stack(self):
        return self.items
