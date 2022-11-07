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
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while 1:
                if data > current.data:
                    if current.right is None:
                        current.right = new_node 
                        break
                    current = current.right
                elif data < current.data:
                    if current.left is None:
                        current.left = new_node 
                        break
                    current = current.left
        return self.root         
 

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def pre(self,node):
        print(node,end=' ')
        if node.left is not None:
            self.pre(node.left)
        if node.right is not None:
            self.pre(node.right)

    def inor(self,node):
        if node.left is not None:
            self.inor(node.left)
        print(node,end=' ')
        if node.right is not None:
            self.inor(node.right)

    def post(self,node):
        if node.left is not None:
            self.post(node.left)
        if node.right is not None:
            self.post(node.right)
        print(node,end=' ')  

    def Breadth(self,node):
        ls=[node]
        while len(ls)!= 0:
            x=ls.pop(0)
            print(x,end=" ")
            if x.left is not None:
                ls.append(x.left)
            if x.right is not None:
                ls.append(x.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root 
for i in inp:
    root = T.insert(i)
print("Preorder : ",end='')
T.pre(root)
print("\nInorder : ",end='')
T.inor(root)
print("\nPostorder : ",end='')
T.post(root)
print("\nBreadth : ",end='')
T.Breadth(root)

