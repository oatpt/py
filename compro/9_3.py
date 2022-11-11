print("*** Maximum Occurrence ***")
lst = [int(e) for e in input("Enter some numbers: ").split()] 
print(max(lst,key=lst.count))