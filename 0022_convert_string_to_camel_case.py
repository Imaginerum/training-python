#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

def camel_case1(text):
    words = text.replace('_','-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])

def camel_case2(text):
    cap = False
    newText = ''
    for t in text:
        if t == '_' or t == '-':
            cap = True
            continue
        else:
            if cap == True:
                t = t.upper()
            newText += t
            cap = False
    return newText

def camel_case3(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("-","_").split("_")])[1:] if text else ''

import re
def camel_case4(text):
    arr = re.split('-|_', text)
    return ''.join(arr[:1] + [t.title() for t in arr[1:]])

def camel_case5(text):
    import re
    return re.sub('[-_](.)', lambda x: x.group()[1].upper(), text)

def camel_case(text):
    import string
    if text != '':
        first = text[0]
        text = text.title()
        text = first + text[1:]
        for i in text:
            if i in string.punctuation:
                text = text.replace(i,'')
        return text
    return text

g = 'japa-jefferson_luz'
print(camel_case(g))