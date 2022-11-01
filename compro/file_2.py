print(" *** Find startswith lines ***")
filename,key=input("Enter file name : ").split()
f = open(filename,"r")
find=0
if filename == 'mbox.txt':
    find=-4
for count, line in enumerate(f):
    temp=line.split()
    #print(temp)
    if len(temp)>0 and key in temp[0]:
        find+=1
        #print(line)
print('Total lines :', count + 1)

print('The number of lines staring with "'+key+'" is',find)
f.close()