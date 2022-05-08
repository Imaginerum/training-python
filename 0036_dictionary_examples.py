# Program which contains grade of a students
# How to use dictionaneres inside a dictionary.

grade_journal = {
    "aksdjashdJ7392HSakak" : {'name' : "Piotr", 'wiek' : 30, 'oceny': (4,5,2,3,4,5,4,5)},
    "ajsdhslakdjklSDHAJ38" : { 'name' : "Karolina", 'wiek' : 28, 'oceny': (5,4,3,2,4,5,6,3)},
    "alsjdlkajskldajslkdj" : { 'name' : "Ewelina", 'wiek' : 22, 'oceny': (4,5,6,4,3,2,1,2,3)}
}
'''
for key in grade_journal:
    print("ID", key,)
    for secondaryKey in grade_journal[key]:
        print(secondaryKey, grade_journal[key][secondaryKey])
'''
'''
for id, dictionary in grade_journal.items():
    print("ID:", id)
    for key in dictionary:
        print(key, ":", dictionary[key])
'''
grade_journal2 = [
    {"id" : "aksdjashdJ7392HSakak", 'name' : "Piotr", 'wiek' : 30, 'oceny': (4,5,2,3,4,5,4,5)},
    {"id" : "ajsdhslakdjklSDHAJ38", 'name' : "Karolina", 'wiek' : 28, 'oceny': (5,4,3,2,4,5,6,3)},
    {"id" : "alsjdlkajskldajslkdj", 'name' : "Ewelina", 'wiek' : 22, 'oceny': (4,5,6,4,3,2,1,2,3)}
]
'''
for key in grade_journal2:
    print()
    for value in key:
        print(value, ":", key[value])
'''
print()

import pprint

print(pprint.pformat(grade_journal2))