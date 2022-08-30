class queue:
    def __init__(self) :
        self.queue=[]
    def enQueue(self,valu):
        self.queue.append(valu)
    def deQueue(self,valu=0):
        return self.queue.pop(valu)
    def isEmpty(self):
        return self.queue==[]
    def size(self):
        return len(self.queue)
    def reverse(self):
        self.queue.reverse()

Normal=queue()
Mirror=queue()
Boom_mirror=queue()
Boom_Mirror_count=0
Boom_Normal_count=0
Failed_Interrupted_count=0
inp1, inp2=input("Enter Input (Normal, Mirror) : ").split()
for i in inp1 :
    Normal.enQueue(i)
for i in inp2 :
    Mirror.enQueue(i)
Mirror.reverse()
check = 1
while check and Mirror.size()>2:
    for i in range(2,Mirror.size()):
        #print(i,Mirror.size())
        if Mirror.queue[i]==Mirror.queue[i-1]==Mirror.queue[i-2]:
            Boom_mirror.enQueue(Mirror.queue[i])
            Boom_Mirror_count+=1
            Mirror.deQueue(i-2)
            Mirror.deQueue(i-2)
            Mirror.deQueue(i-2)
            break
        elif i==Mirror.size()-1:
            check=0
#print(Mirror.queue)
check = 1
while check and Normal.size()>2:
    for i in range(2,Normal.size()):
        #print(i,Normal.size())
        if Normal.queue[i]==Normal.queue[i-1]==Normal.queue[i-2]:
            if not Boom_mirror.isEmpty():
                if Normal.queue[i] == Boom_mirror.queue[0]:
                    Boom_mirror.deQueue()
                    Failed_Interrupted_count+=1
                    Normal.deQueue(i-2)
                    Normal.deQueue(i-2)
                    break
                else:
                    Normal.queue.insert(i,Boom_mirror.deQueue())
                    break
            else:
                Boom_Normal_count+=1
                Normal.deQueue(i-2)
                Normal.deQueue(i-2)
                Normal.deQueue(i-2)
                break
        elif i==Normal.size()-1:
            check=0
Normal.reverse()   
Mirror.reverse()
print("NORMAL :")    
print(Normal.size())
for i in Normal.queue: 
    print(i,end='')
if Normal.isEmpty():
    print("Empty",end='')
print("\n"+str(Boom_Normal_count)+" Explosive(s) ! ! ! (NORMAL)")
if Failed_Interrupted_count>0:
    print("Failed Interrupted",Failed_Interrupted_count,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(Mirror.size())
for i in Mirror.queue: 
    print(i,end='')
if Mirror.isEmpty():
    print("ytpmE",end='')
print("\n(RORRIM) ! ! ! (s)evisolpxE",Boom_Mirror_count)





