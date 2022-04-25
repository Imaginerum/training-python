# Tuple in sets:

guestList = {
    ('Arkadiusz', 29, "mężczynza"),
    ('Ewelina', 24, "kobieta"),
    ('Paweł', 45, 'mężczyzna')
}
guestList2 = {
    ('Karol', 17, 'mężczyzna'),
    ('Paweł', 45, 'mężczyzna'),
    ('Kamil', 28, 'mężczyzna')
}
"""
You can use to manage sets: &, |, ^, -
"""
print(guestList ^ guestList2)

for name, age, gender in guestList:
    print(name)
    print(age)
    print(gender, end='\n\n')

