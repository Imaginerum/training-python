#The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

def d_encoder1(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

from collections import Counter

def d_encoder2(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

def d_encoder3(word):
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) >1:
            result += ")"
        else:
            result += "("
    return result

def d_encoder(word):
    new_string = ""
    word = word.lower()
    for char in word:
        new_string += (")" if word.count(char) > 1 else "(")

    return new_string

w = "suspension"
print(d_encoder(w))