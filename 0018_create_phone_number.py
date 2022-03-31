#Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

def number1(s):
    return "({}{}) {}{}{}-{}{}{}-{}{}{}".format(*s)

def number2(s):
    str1 = ''.join(str(x) for x in s[0:2])
    str2 = ''.join(str(x) for x in s[2:5])
    str3 = ''.join(str(x) for x in s[5:8])
    str4 = ''.join(str(x) for x in s[8:11])
    return '({}) {}-{}-{}'.format(str1, str2, str3, str4)

def number3(s):
    m = ''.join(map(str, n))
    return f"({m[:2]}) {m[2:5]}-{m[5:8]}-{m[8:11]}"

def number4(s):
    s = "".join([str(x) for x in s])
    return ("("+str(s[0:2])+ ") " + str(s[2:5])+"-"+str(s[5:8]) + "-" + str(s[8:]))


def number5(n):
    d = '('
    for i in range(len(n)):
        if i < 2:
            d += str(n[i])
            if i == 1:
                d += ') '
        elif i>=2 and i <5:
            d += str(n[i])
            if i == 4:
                d += '-'
        elif i>=5 and i<8:
            d += str(n[i])
            if i == 7:
                d += '-'
        elif i >=8 and i<11:
            d += str(n[i])
    return d


n=str(58456789765)
print(number(n))