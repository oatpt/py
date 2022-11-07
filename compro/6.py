x = list(input("*** Shopping List 2 ***\nEnter some pairs of (operation, item): ").split(','))

def shopping(state,key):
    if key not in shopping_dict.keys():
        shopping_dict[key] = 1
    elif state == 1:
        shopping_dict[key] += 1
    elif state == 2:
        shopping_dict[key] -= 1

    if shopping_dict[key] == 0:
        shopping_dict.pop(key)
    return shopping_dict

shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}
for i in x :
    i = i.lower()
    if i[0:2] == 'a ':
        state = 1
    elif i[0:2] == 'r ':
        state = 2
    else:
        state = 99
        break    
    if i[2:] != '':
        key = i[2:]
        shopping(state,key)
    else:
        state = 99
        break
if state != 99:
    print("Final shopping dict is",shopping_dict)
else:
    print("Operation not supported!")