print("*** Shopping List 2 ***")
shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}
inp = input("Enter some pairs of (operation, item): ").split(',')
for i in inp:
    a,b=i.split()
    b=b.lower()
    if a=='a':
        if b not in shopping_dict:
            shopping_dict[b]=1
        else :
            shopping_dict[b]+=1
    elif a=='r':
        if b in shopping_dict:
            shopping_dict.pop(b)
    else :
        print("Operation not supported!")
        exit()
print("Final shopping dict is",shopping_dict)