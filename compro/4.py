def less (x,y):
    return x<y
a,b=input().split()
a=int(a)
b=int(b)
if less(a,b):
    print(b,"more than",a)
else:
    print(a,"more than",b)