print(" *** Find Empty lines ***")
filename=input("Enter file name : ")
f = open(filename,"r")
empty=0
for count, line in enumerate(f):
    if line=="\n":
        empty+=1
print("Empty lines =>",empty)
print('Total lines =>', count + 1)
f.close()