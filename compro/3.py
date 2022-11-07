x=int(input())
for i in range(x):
    for k in range(x):  #1
        if i+k==x-1:
            print("/",end='')
        else:
            print("",end=' ')
    for k in range(x):  #2
        if i==k:
            print("\\",end='')
        else:
            print("",end=' ')
    print()
for i in range(x):
    for k in range(x):  #3
        if i==k:
            print("\\",end='')
        else:
            print("",end=' ')
    for k in range(x):  #4
        if i+k==x-1:
            print("/",end='')
        else:
            print("",end=' ')
    print()
    