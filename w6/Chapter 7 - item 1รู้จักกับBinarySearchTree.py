class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(data,self.root)
        return self.root

    def _insert(self, data,node):
        if node is None:
            return Node(data)
        if data<node.data:
            node.left=self._insert(data,node.left)
        elif data>node.data:
            node.right=self._insert(data,node.right)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root 
for i in inp:
    root = T.insert(i)
T.printTree(root)
