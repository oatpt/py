print(" *** Find number of lines for specific word ***")
filename,key=input("Enter file name and word : ").split()
f = open(filename,"r")
find=0
if filename == 'mbox.txt':
    find=-4
for count, line in enumerate(f):
    if key in line:
        find+=1

print('Number of lines having "'+key+'" =>',find)
print('Total lines =>', count + 1)
f.close()