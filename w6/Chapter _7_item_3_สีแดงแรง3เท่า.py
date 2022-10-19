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

    def red(self,node,data):
        if node != None:
            self.red(node.right, data)
            if node.data>data:
                node.data*=3
            self.red(node.left,data) 
    
T = BST()
temp=input('Enter Input : ').split('/')
inp = [int(i) for i in temp[0].split()]
root = T.root 
for i in inp:
    root = T.insert(i,root)
T.printTree(root)
T.red(root,int(temp[1]))
print("--------------------------------------------------")
T.printTree(root)
