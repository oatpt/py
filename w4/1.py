class LinkedList:
    
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def __str__(self) :
        self.str=""
        self.now=self.head
        for i in range(self.size):
            self.str+=str(self.now.data)
            if i != self.size-1:
                self.str+="->"
            self.now=self.now.next
        return self.str

    def isEmpty(self) :
        return self.size==0
    
    def append(self,data):
        self.newnode=self.Node(data)
        if self.size==0:
            self.head=self.newnode
        else :
            self.tail.next=self.newnode
        self.tail=self.newnode
        self.size+=1

    def insert(self,index,data):
        self.newnode=self.Node(data)
        if 0<=index<=self.size:
            print("index =",index,"and data =",data)
            if index==0:
                self.newnode.next=self.head
                self.head=self.newnode
            else:
                self.now=self.head
                self.i=1
                while self.i<index:
                    self.now=self.now.next
                    self.i+=1
                if self.size!=index:
                    self.newnode.next=self.now.next
                else:
                    self.tail=self.newnode
                self.now.next=self.newnode
            self.size+=1
        else :
            print("Data cannot be added")

List=LinkedList()
inp=list(input("Enter Input : ").split(','))
for i in inp[0].split():
    i=int(i)
    List.append(i)
print(List)
for i in range(1,len(inp)):
    List.insert(int(inp[i][1]),int(inp[i][3]))
    print(List)

