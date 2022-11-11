print("*** Shopping List ***")
ls = ["egg", "ham", "water", "soda"]
inp = input("Enter some pairs of (operation, item): ").split(',')
for i in inp:
    a,b=i.split()
    b=b.lower()
    if a=='a':
        if b not in ls:
            ls.append(b)
    elif a=='r':
        if b in ls:
            ls.remove(b)
    else :
        print("Operation not supported!")
        exit()
print("Final shopping list is",ls)