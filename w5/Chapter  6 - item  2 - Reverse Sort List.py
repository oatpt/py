def sort(ls,index):
    if index <= 0:
        return
    
    if(ls[index]<ls[index-1]):
        ls[index],ls[index-1]=ls[index-1],ls[index]
    sort(ls,index-1)
    
    
    if(ls[index]<ls[index-1]):
        ls[index],ls[index-1]=ls[index-1],ls[index]
    sort(ls,index-1)

inp=[int(e) for e in list(input('Enter your List : ').split(','))]
sort(inp,len(inp)-1)
print('List after Sorted :',inp)