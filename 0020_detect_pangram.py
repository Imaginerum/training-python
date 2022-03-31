#A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

import string
print(string)

def is_pangram1(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

import string
def is_pangram2(s):
    s = s.lower()
    return set(string.ascii_lowercase).issubset(s)

def is_pangram3(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True

def is_pangram4(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False


f = 'ajhsdkjaHfeWuipwnYKlsxaxgasdqwebcnoprtvnzmxcks'
print(is_pangram(f))