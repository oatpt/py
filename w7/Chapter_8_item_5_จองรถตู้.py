class box:
    def __init__(self,number) -> None:
        self.time=0
        self.number=number

def update(n):
    for i in range(n):
        for k in range(i+1,n):
            if van[k].time<van[i].time:
                van[k],van[i]=van[i],van[k]
            elif van[k].time==van[i].time and van[k].number<van[i].number:
                van[k],van[i]=van[i],van[k]

a,b=input("Enter Input : ").split('/')
inp=[int(e) for e in b.split()]
a=int(a)
van=[]
for i in range(a):
    van.append(box(int(i)+1))

for i in range(len(inp)):
    print("Customer",i+1,"Booking Van",van[0].number,"|",inp[i],"day(s)")
    van[0].time+=inp[i]
    update(a)
