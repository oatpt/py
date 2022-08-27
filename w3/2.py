text=input("Enter expresion : ")
stack=[]
for i in text:
    if i in '{[(':
        stack.append(i)
    elif i in '}])': 
        if len(stack)>0:
            if i==']'and stack[-1]=='[':
                stack.pop()
            elif i=='}'and stack[-1]=='{':
                stack.pop()
            elif i==')'and stack[-1]=='(':
                stack.pop()
            else:
                print(text+" Unmatch open-close  ")
                exit()
        else :
            print(text+" close paren excess")
            exit()

print(text,end='')
if len(stack)>0 :
    print(" open paren excess%4d : "%len(stack) ,end='')
    for i in stack:
        print(i,end='')
