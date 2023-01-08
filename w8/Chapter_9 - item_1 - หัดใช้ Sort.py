inp =[int(e) for e in input("Enter Input : ").split()]
ls=inp.copy()
for i in range(len(ls)):
    for k in range(len(ls)-1):
        if ls[k]>ls[k+1]:
            ls[k],ls[k+1]=ls[k+1],ls[k]
if ls==inp:
    print("Yes")
else:
    print("No")
