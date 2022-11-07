print(" *** Data type integer float string ***")
x = input("Enter a word : ")
try :
    x=float(x)
    if x//1==x:
        x=int(x)
        print(x,"* 2 =",x*2)
    else:
        print("%.3f"%x,"/ 3 =","%.3f"%(x/3))

except:
    print(x,x,x)

