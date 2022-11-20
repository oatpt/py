t=("Fusce","vehicula"  ,"mattis" ,"eleifend" ,"condimentum" ,"nisl" ,"sit" ,"amet" ,"magna" ,"semper" ,"pharetra" ,"Proin" ,"aliquet" ,"magna" ,"non" ,"dapibus" ,"blandit","Quisque" ,"nibh")
print(" *** Tuple Search ***")
x=input("Enter a word : ")
if x in t:
    print("\nIndex of word '"+x+"' is",t.index(x))
else:
    print("\nWord '"+x+"' not found in Tuple")