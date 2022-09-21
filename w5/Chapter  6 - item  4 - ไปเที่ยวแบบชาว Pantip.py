def pantip(k, n, arr, path):
    #print(path,k)
    #rint(n)
    sum=0
    if k==0:
        print(*path)
        #for i in path:
        #    print(i,end=' ')
        #print()
        return 1
    if n>=len(arr):
        return 0
    elif k-arr[n]>=0:
        temp=path.copy()
        temp.append(arr[n])
        sum=pantip(k-arr[n], n+1, arr, temp)

    return sum+pantip(k, n+1, arr, path)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))