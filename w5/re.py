def palin(L,R):
    #base
    if L >= R:
        return 1
    if not ls[L].isalpha() and not ls[L].isdigit():
        return palin(L+1,R)
    if not ls[R].isalpha() and not ls[R].isdigit():
        return palin(L,R-1)
    if ls[L] == ls[R]:
        return palin(L+1,R-1)
    return 0
ls="asdfds+5a"
if palin(0,len(ls)-1):
    print("is palindom")
else:
    print("not palindom")
