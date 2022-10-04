class LinkList :
    class Node :
        def __init__ (self,element) :
            self.element = element
            self.next = None 
            self.previous = None
    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0 

    def append(self,data) :
        new = self.Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            self.tail.next = new
            new.previous = self.tail
            self.tail = new
        self.size += 1
            

    def isEmpty(self):
        return self.head == None

    def size(self) :
        return self.size

    def insert(self, index, data):
        new = self.Node(data)
        x = self.head
        id = 0
        if index < 0 :
            print("Data cannot be added")
        elif index == 0 :
            print("index = 0 and data =",data)
            self.add_head(data)
        elif self.isEmpty() and index != 0 :
            print("Data cannot be added")
        elif index > self.size() :
            print("Data cannot be added")
        elif index == self.size() :
            print("index =",index,"and data =",data)
            self.append(data)
        else :
            while id != index-1 :
                x = x.next
                id+=1
            #print(x.element)
            y=x.next
            x.next = new
            y.previous = new
            new.next = y
            new.previous = x        
            print("index =",index,"and data =",data)
            self.size += 1

    def remove(self, data):
        count = 0
        x = self.head
        if x != None :
            if x.element == data :
                print("removed :",data,"from index :",0)
                if self.head == self.tail :
                    self.head = None
                    self.tail = None 
                    self.size = 0
                    return
                else : 
                    self.head = x.next
                    x = x.next
                    x.previous = None
                    self.size -= 1
                    return
        while x != None :
            if x.element == data :
                break
            y = x
            x = x.next
            count += 1
        if x == None :
            print("Not Found!")
            return
        elif x.next == None :
            self.tail = y
            y.next = None
        else :
            y.next = x.next
            x = x.next
            x.previous = y
        self.size -= 1
        print("removed :",data,"from index :",count)

    def add_head(self,data) :
        new = self.Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            x = self.head
            new.next = x
            x.previous = new
            self.head = new
            
    def str_reverse(self) :
        x = self.tail
        while x != None :
            if x.previous != None :
                print(x.element,end="->")
            else :
                print(x.element,end=" ")
            x = x.previous
            
    def __str__(self) :
        x = self.head
        while x != None :
            if x.next != None :
                print(x.element,end="->")
            else :
                print(x.element,end=" ")
            x = x.next

list = LinkList()
inp = input("Enter Input : ").split(",")

for ele in inp :
    ele = ele.strip()
    if ele[0] == "A" and ele[1] == "b":
        ab = ele.split()
        list.add_head(int(ab[1]))
    elif ele[0] == "I" :
        i1 = ele.split()
        i2 = i1[1].split(":")
        list.insert(int(i2[0]),int(i2[1]))
    elif ele[0] == "A" :
        n = ele.split()
        list.append(int(n[1]))
    else :
        r = ele.split()
        list.remove(int(r[1]))

    print("linked list : ",end="")
    list.__str__()
    print()
    print("reverse : ",end="")
    list.str_reverse()
    print()