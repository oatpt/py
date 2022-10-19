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
        self.check = 0

    def insert(self, data,node):
        if node is None:
            self.check=0
            return Node(data)
        if not node.data.isalpha() and self.check==1:
            node.right=self.insert(data,node.right)
        if not node.data.isalpha() and self.check==1:
            node.left=self.insert(data,node.left)
        return node
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
    
    def pre (self,node):
        print(node,end='')
        if node.left is not None:
            self.pre(node.left)
        if node.right is not None:
            self.pre(node.right)
    
    def in_or (self,node):
        
        if node.left is not None:
            print("(",end='')
            self.in_or(node.left)
        print(node,end='')
        if node.right is not None:
            self.in_or(node.right)
            print(")",end='')       
    
T = BST()
inp = input('Enter Postfix : ')
root=T.root
temp=[]
for i in inp:
    temp.append(i)
while len(temp):
    x=temp.pop()
    T.check=1
    root = T.insert(x,root)
print("Tree :")
T.printTree(root)
print("--------------------------------------------------")
print("Infix : ",end='')
T.in_or(root)
print("\nPrefix : ",end='')
T.pre(root)



