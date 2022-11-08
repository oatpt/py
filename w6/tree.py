'''
 * กลุ่มที่  : 22010119
 * 64010635 ไพฑูรย์ ทองมีศรีสุข
 * chapter : 7	item : 1	ครั้งที่ : 0001
 * Assigned : Monday 10th of October 2022 08:27:50 PM --> Submission : Tuesday 18th of October 2022 08:06:09 PM	
 * Elapsed time : 11498 minutes.
 * filename : Chapter 7 - item 1รู้จักกับBinarySearchTree.py
'''
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
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root 
for i in inp:
    root = T.insert(i,root)
T.printTree(root)
