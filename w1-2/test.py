from statistics import mode


print("*** Election ***")
n=input("Enter a number of voter(s) : ")
ls=[int(e) for e in input().split() if 0<int(e)<21]
print(ls)
"""newls=[]
for i in ls:
    if 0<i<21:
        newls.append(i)
if len(newls)>0:
    print(mode(newls))
else:
    print("*** No Candidate Wins ***")"""
