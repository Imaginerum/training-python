#ZAD: Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').


def solution1(s):
    result = []
    if len(s) % 2: s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

import re
def solution2(s):
    return re.findall(".{2}", s + "_")

def solution3(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution4(s):
    return [(s + "_")[i:i+2] for i in range(0, len(s), 2)]

def solution5(s):
    if len(s) % 2 == 1:
        s += '_'
    return [s[i:i+2] for i in range(0,len(s),2)]

import re

def solution6(s):
    return re.findall('..', s + '_')

def solution7(s):
    if len(s) == 0:
        return[]
    elif len(s) == 1:
        return [s+'_']
    else:
        return [s[:2]] + solution7(s[2:])

def solution8(s):
    s = s + '_' if (len(s)%2 == 1) else s
    return [s[i:i+2] for i in range(0, len(s), 2)]

def solution9(s):
    if len(s) == 1:
        return [s+"_"]
    elif len(s) == 0:
        return []
    return [s[0] + s[1]] + solution9(s[2:])

x= 'askJSKdnakd'
print(solution9(x))