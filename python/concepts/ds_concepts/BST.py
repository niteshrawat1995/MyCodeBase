# Binary Search Tree
# Duplicates not allowed.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, cur_node, val):
        if val < cur_node.data:
            if cur_node.leftchild is None:
                cur_node.leftchild = Node(val)
            else:
                self._insert(cur_node.leftchild, val)
        else:
            if cur_node.rightchild is None:
                cur_node.rightchild = Node(val)
            else:
                self._insert(cur_node.rightchild, val)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder(self.root, '')

    def preorder(self, start, traversal):
        # Root->Left->Right
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.preorder(start.leftchild, traversal)
            traversal = self.preorder(start.rightchild, traversal)
        return traversal

    def inorder(self, start, traversal):
        # Left->Root->Right
        if start:
            traversal = self.inorder(start.leftchild, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.inorder(start.rightchild, traversal)
        return traversal

    def size_of_tree(self):
        # size_of_tree = Total number of nodes in the tree.
        # We'll maintain a stack and push the root on it(if present).
        # Pop the node and if childrens are present , push them into the stack.
        # Increment the counter on pushing of every node.
        # Repeat till the stack gets empty. And return counter.
        if self.root is None:
            return 0
        # Using a list as stack here.
        else:
            size = 1  # size root is present.
            stack = []
            stack.append(self.root)
            while len(stack) != 0:
                node = stack.pop()
                if node.leftchild:
                    size += 1
                    stack.append(node.leftchild)
                if node.rightchild:
                    size += 1
                    stack.append(node.rightchild)
            return size

    def is_BST(self):
        if self.root:
            is_satisfied = self._is_BST(self.root, self.root.data)
            if is_satisfied is None:
                return True
            else:
                return False
        return True

    def _is_BST(self, cur_node, data):
        if cur_node.leftchild:
            if data > cur_node.leftchild.data:
                return self._is_BST(cur_node.leftchild, cur_node.leftchild.data)
            else:
                return False
        if cur_node.rightchild:
            if data > cur_node.rightchild.data:
                return self._is_BST(cur_node.rightchild, cur_node.rightchild.data)
            else:
                return False



        # Driver:
bst = Tree()

bst.insert(27)
bst.insert(14)
bst.insert(19)
bst.insert(10)
bst.insert(35)
bst.insert(31)
bst.insert(42)

print(bst.size_of_tree())
# print(bst.print_tree('inorder'))

print(bst.is_BST())
