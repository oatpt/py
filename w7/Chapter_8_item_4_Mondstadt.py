class box:
    def __init__(self,number,pow) -> None:
        self.pow=pow
        self.number=number

def findpow(i):
    if i<len(knight):
        return knight[i].pow+findpow(2*i+1)+findpow(2*i+2)
    return 0

a,b=input("Enter Input : ").split('/')
inp=[int(e) for e in a.split()]
T=b.split(',')
knight=[]
for i in range(len(inp)):
    knight.append(box(0,inp[i]))
print(findpow(0))
for i in T:
    x,y=i.split()

    print(x,end='')
    if findpow(int(x))>findpow(int(y)):
        print(end='>')
    elif findpow(int(x))<findpow(int(y)):
        print(end='<')
    else:
        print(end='=')
    print(y)
