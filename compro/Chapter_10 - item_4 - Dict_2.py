dic = {'Tesla': 10, 'Ford': 50, 'Toyota': 20, 'Honda': 80}
inp = input("Enter : ").split()
print("dict_old =",dic)
while len(inp):
    a=inp.pop(0)
    b=int(inp.pop(0))
    if a in dic and dic[a]>=b:
        dic[a]-=b
        print(a,"exists in dicts")
        print("dict_new =",dic)
    else:
        print(a,"does not exist")