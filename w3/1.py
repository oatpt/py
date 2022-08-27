stack=[]
ls=input("Enter Input : ").split(',')
for i in ls:
    if i =='P':
        if len(stack)>0:
            print("Pop =",stack[-1],"and Index =",len(stack)-1)
            stack.pop()
        else:
            print("-1")
    else:
        a,b=i.split()
        stack.append(b)
        print("Add =",b,"and Size =",len(stack))
print("Value in Stack = ",end='')        
if len(stack)>0:
    for i in stack:
        print(i,end=' ')
else:
    print("Empty")
