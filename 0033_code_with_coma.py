# Built program witch will produce string separated by coma and the last name will have "and" separator.

spam = ['jabłka','bananay','tofu','koty',]

def code_separator(spam):

    spam = ', '.join(spam[:-1]) + ' i ' + spam[-1]
    print(spam)

code_separator(spam)

