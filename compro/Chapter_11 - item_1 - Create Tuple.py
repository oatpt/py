print(" *** Create Tuple ***")
x=int(input("Enter a number : "))
t=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
for i in range(x):
    for k in range(i+1):
        print(t[k],end=' ')
    print()