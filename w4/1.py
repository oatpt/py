class LinkedList:
    
    class Node:
        
        def __init__(self, data=None):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head=None
        self.size=0
    
    def __str__(self) :
        
        text="link list : "
        now=self.head
        for i in range(self.size):
            text+=str(now.data)
            if i != self.size-1:
                text+="->"
            now=now.next
        if self.size==0 :
            return 'List is empty'
        return text

    def isEmpty(self) :
        return self.size==0
    
    def append(self,data):
        newnode=self.Node(data)
        if self.size==0:
            self.head=newnode
        else :
            x=self.head
            while x.next!=None:
                x=x.next
            x.next=newnode
        self.size+=1

    def insert(self,index,data):
        newnode=self.Node(data)
        if 0<=index<=self.size:
            print("index =",index,"and data =",data)
            if index==0:
                newnode.next=self.head
                self.head=newnode
            else:
                x=self.head
                i=1
                while i<index:
                    x=x.next
                    i+=1
                newnode.next=x.next
                x.next=newnode
            self.size+=1
        else :
            print("Data cannot be added")
        
    def pop(self,pos=-1):
        if pos == -1 :
            pos = self.size-1
        x=self.head
        if pos == 0:
            self.head=x.next
            self.size-=1
        elif pos<self.size:
            for i in range(pos-1):
                x=x.next
            y=x.next
            x.next=y.next
            self.size-=1
        else:
            print('error')
        
            
        

List=LinkedList()
# inp=list(input("Enter Input : ").split(','))
# for i in inp[0].split():
#     i=int(i)
#     List.append(i)
# print(List)
# for i in range(1,len(inp)):
#     temp = inp[i].split(':')
#     List.insert(int(temp[0]),int(temp[1]))
#     print(List)
List.append(0)
List.append(1)
List.append(2)
List.append(3)
List.append(4)
List.append(5)
print(List)
List.pop(2)
print(List)
List.pop()
print(List)


