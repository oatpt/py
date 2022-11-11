print(" *** Median Mean ***")
lst = [int(e) for e in input("Enter numbers : ").split()] 
print("list = ",lst)
if (sum(lst)/len(lst))%1>0:
    print("Mean = %.2f"%(sum(lst)/len(lst)))
else:
    print("Mean =  %d"%(sum(lst)/len(lst)))
lst.sort()
print("sort list =",lst)
if(len(lst)%2==0):
    if ((lst[len(lst)//2]+lst[len(lst)//2-1])/2)%1>0:
        print("Median = %.2f"%((lst[len(lst)//2]+lst[len(lst)//2-1])/2))
    else:
        print("Median =  %d"%((lst[len(lst)//2]+lst[len(lst)//2-1])/2))
else:
    if lst[len(lst)//2]%1>0:
        print("Median = %.2f"%(lst[len(lst)//2]))
    else:
        print("Median =  %d"%(lst[len(lst)//2]))

