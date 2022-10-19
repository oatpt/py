
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

    def insert(self,data):
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
    
    def checkpos(self,data):
        if data == self.root.data:
            print("Root")
            return
        _checkpos(data,self.root)

def _checkpos(data,node):
    if node is None:
        print("Not exist")
        return 
    if data<node.data:
        _checkpos(data,node.left)
    elif data>node.data:
        _checkpos(data,node.right)
    else:
        if node.right is None and node.left is None:
            print("Leaf")
        else:
            print("Inner")

    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
