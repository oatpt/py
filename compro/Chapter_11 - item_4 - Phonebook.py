my_phonebook = (
    ('Ana', '012345678'),
    ('Bob', '012345677'),
    ('Cathelyn', '012345676'),
    ('Dylan', '012345675'),
    ('Ethan', '012345674'),
    ('Fritz', '012345673'),
    ('George', '012345672'),
    ('Helena', '012345671'),
    ('Ivanovich', '021234567'),
    ('Jason', '021234566'),
    ('Kevin', '021234565'),
    ('Lisa', '021234564'),
    ('Marcus', '021234563'),
    ('Neil', '021234562'),
    ('Ophra', '021234561'),
    ('Persie', '031234569'),
    ('Quentin', '031234568'),
    ('Russell', '031234567'),
    ('Steve', '031234566'),
    ('Tsar', '031234565'),
    ('Uamee', '031234564'),
    ('Vega', '031234563'),
    ('Wallis', '031234562'),
    ('Xen', '031234561'),
    ('Yves', '041234569'),
    ('Zed', '061234568')
)
x = input("Who you want to call: ")
for i in my_phonebook:
    if x.lower()==i[0].lower():
        print(i[0]+"'s number is "+i[1])
        exit()
print("Can't find "+x.title()+" in your phonebook")