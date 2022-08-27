def mod_position(arr, s):
    ans=[]
    for i in range(s,len(arr)+1,s):
        ans.append(arr[i-1])
    return ans

print("*** Mod Position ***")
text,num=input("Enter Input : ").split(',')
print(mod_position(text, int(num)))
