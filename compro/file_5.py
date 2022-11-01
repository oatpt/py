print(" *** File Error Handling ***")
filename,key=input("Enter file name and word : ").split()
try:
    f = open(filename,"r")
    
    find=0
    sum=0
    for count, line in enumerate(f):
        if key in line:
            find+=1
            sum+=int(count)+1

    print('Number of lines having "'+key+'" =>',find)
    print("Sum of line number =>",sum)
    print('Total lines =>', count + 1)
    f.close()
except:
    print("Error can not open file => "+filename)
       