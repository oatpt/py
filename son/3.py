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

    def high(self,node):
        l=0 #ถ้าต้องการให้เป็น012ให้เปลี่ยนเป็น-1
        r=0
        if node.right is not None:
            r = self.high(node.right)
        if node.left is not None:
            l = self.high(node.left)
        if r>=l:
            return r+1
        elif r<l:
            return l+1
                
    def size(self,node):
        l=0
        r=0
        if node.right is not None:
            r = self.size(node.right)
        if node.left is not None:
            l = self.size(node.left)
        return (l+r)+1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def red(self, node,data):
        if node != None:
            self.red(node.left,data)
            if int(node.data) > int(data):
                node.data*=3
            self.red(node.right,data)

T = BST()
inpu,k = input('Enter Input : ').split('/')
inp = [int(i) for i in inpu.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.red(root,k)
T.printTree(root)


