class stack:
    def __init__(self):
        self.stack=[]
    def push(self,valu):
        self.stack.append(valu)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.stack==[]
    def size(self):
        return len(self.stack)

s=stack()
print(s.isEmpty())
for i in range(10):
    s.push(i)
print(s.isEmpty())
print("peek1+++",s.peek())
print(s.pop())
print("peek2+++",s.peek())
print(s.stack)
print(s.size())

