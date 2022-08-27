class Stack:
    stack=[]
    size=0
    def __init__(self) :
        self.stack=[]
        self.size=0
    def push(self,x):
        while self.size>0 and x>=self.stack[-1]:
            self.stack.pop()
            self.size-=1
        self.stack.append(x)
        self.size+=1
    def size(self):
        return self.size
        

S = Stack()


inp = input('Enter Input : ').split(',')
for i in inp:
    if i =='B':
        print(S.size)
    else:
        a,b=i.split()
        S.push(int(b))
