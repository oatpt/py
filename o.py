def sort(index, lst): #index = ตำแหน่ง
   

def sumls(ans,index):
    
x,inp=input("Enter Input : ").split('/')
x=int(x)
ls=[int(e) for e in inp.split()]
sort(len(ls)-1,ls)
temp=[]
sumls([],0)
for i in range(len(temp)):
    for k in range(len(temp)-1):
        if len(temp[k])>len(temp[k+1]):
            temp[k],temp[k+1]=temp[k+1],temp[k]
for i in temp:
    print(i)
if temp == []:
    print("No Subset")