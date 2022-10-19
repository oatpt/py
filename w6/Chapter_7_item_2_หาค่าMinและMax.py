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

    def insert(self, data,node):
        if node is None:
            return Node(data)
        if data<node.data:
            node.left=self.insert(data,node.left)
        elif data>node.data:
            node.right=self.insert(data,node.right)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
    
    def MAX(self,node):
        MAX=node.data
        if node.right is not None:
            temp=self.MAX(node.right)
            if MAX<temp:
                MAX=temp
        if node.left is not None:
            temp=self.MAX(node.left) 
            if MAX<temp:
                MAX=temp
        return MAX

    def MIN(self,node):
        MIN=node.data
        if node.right is not None:
            temp=self.MIN(node.right)
            if MIN>temp:
                MIN=temp
        if node.left is not None:
            temp=self.MIN(node.left) 
            if MIN>temp:
                MIN=temp
        return MIN
    
T = BST()
temp=input('Enter Input : ').split('|')
inp = [int(i) for i in temp[0].split()]
root = T.root 
for i in inp:
    root = T.insert(i,root)
T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.MIN(root))
print("Max :",T.MAX(root))
