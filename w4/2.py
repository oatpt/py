class LinkedList:
    
    class Node:
        
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
    
    def __init__(self):
        self.head=self.Node(None)
        self.tail=self.head
        self.size=0
    
    def __str__(self) :
        self.str="link list : "
        self.now=self.head.next
        for i in range(self.size):
            self.str+=str(self.now.data)
            if i != self.size-1:
                self.str+="->"
            self.now=self.now.next
        return self.str

    def str_reverse(self):
        self.str="reverse : "
        self.now=self.tail
        for i in range(self.size):
            self.str+=str(self.now.data)
            if i != self.size-1:
                self.str+="->"
            self.now=self.now.previous
        return self.str
        
    def isEmpty(self) :
        return self.size==0
    
    def append(self,data):
        self.newnode=self.Node(data)
        self.newnode.previous=self.tail
        self.tail.next=self.newnode
        self.tail=self.newnode
        self.size+=1

    def insert(self,index,data):
        self.newnode=self.Node(data)
        if 0<=index<=self.size:
            print("index =",index,"and data =",data)
            self.now=self.head
            self.i=0
            while self.i<index:
                self.now=self.now.next
                self.i+=1
            if self.size!=index:
                self.now.next.previous=self.newnode
                self.newnode.next=self.now.next
                self.now.next=self.newnode
                self.newnode.previous=self.now
            else:
                self.tail=self.newnode
                self.now.next=self.newnode
                self.newnode.previous=self.now
            self.size+=1
        else :
            print("Data cannot be added")
            
    def remove(self, data):
        try :
            self.now=self.head.next
            i=0
            while self.now!=self.tail:
                if self.now.data==data:
                    self.now.previous.next=self.now.next
                    self.now.next.previous=self.now.previous
                    print ('removed :',data,'from index :',i)
                    self.size-=1
                    return 
                else:
                    self.now=self.now.next
                    i+=1
            if self.now.data==data:
                    self.now.previous.next=self.now.next
                    self.now.next.previous=self.now.previous
                    print ('removed :',data,'from index :',i)
                    self.size-=1
                    return
            else :
                print("Not Found!")
        except:
            print("Not Found!")



List=LinkedList()
inp=list(input("Enter Input : ").split(','))
for i in inp:
    x = i.split(' ')
    if(x[0]=='A'):
        List.append(int(x[1]))
    elif(x[0]=='Ab'):
        List.insert(int(x[1]),0)  
    elif(x[0]=='I'):
        temp = x[1].split(':')
        List.insert(int(temp[0]),int(temp[1]))
    elif(x[0]=='R'):
        List.remove(int(x[1]))
    print(List)
    print(List.str_reverse())
#List.append(1)
#print(List)