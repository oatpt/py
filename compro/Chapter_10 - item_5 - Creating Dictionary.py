print(" *** Creating Dictionary ***")
dic={}
inp = input("Enter text : ").split()
while len(inp):
    a=inp.pop(0)
    b=int(inp.pop(0))
    if a not in dic:
        dic[a]=b
    else :
        dic[a]+=b
print(dic)