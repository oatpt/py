class Node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return self.data #โซยากมากค่าาา
    
class tree:
    def __init__(self) :
        self.root=None
    
    def __str__(self):
        if self.root is None:
            return "ไม่ทำแล้ว"
        else:
            

    def insert(self,data):
        new=Node(data)
        if self.root is None:
            self.root=new
        else:
            current=self.root
            while current is not None:
                if data>current.data:
                    current=current.right
                    break
                elif data<current.data:
                    current=current.left
                    break
            current=new
            