#ZAD. zamiana liczb całkowitych na liczby rzymskie

n=2222

def solution1(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution1(n))

vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution2(n):
    if n == 0: return ""
    return next(c + solution2(n-v) for c,v in vals if v <= n)


units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution3(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]


anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution4(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)

def solution5(n):
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while (a <= n):
            n = n - a;
            roman = roman + dic[a];
    return roman

def solution6(n):
    s = ''
    while (n - 1000 >= 0):
        n = n - 1000
        s += 'M'
    while (n - 900 >= 0):
        n = n - 900
        s += 'CM'
    while (n - 500 >= 0):
        n = n - 500
        s += 'D'
    while (n - 400 >= 0):
        n = n - 400
        s += 'CD'
    while (n - 100 >= 0):
        n = n - 100
        s += 'C'
    while (n - 90 >= 0):
        n = n - 90
        s += 'XC'
    while (n - 50 >= 0):
        n = n - 50
        s += 'L'
    while (n - 40 >= 0):
        n = n - 40
        s += 'XL'
    while (n - 10 >= 0):
        n = n - 10
        s += 'X'
    while (n - 9 >= 0):
        n = n - 9
        s += 'IX'
    while (n - 5 >= 0):
        n = n - 5
        s += 'V'
    while (n - 4 >= 0):
        n = n - 4
        s += 'IV'
    while (n - 1 >= 0):
        n = n - 1
        s += 'I'
    return s

def solution7(n):
    return  " M MM MMM".split(" ")[n//1000] + \
            " C CC CCC CD D DC DCC DCCC CM".split(" ")[n//100%10] + \
            " X XX XXX XL L LX LXX LXXX XC".split(" ")[n//10%10] + \
            " I II III IV V VI VII VIII IX".split(" ")[n%10]

def solution8(x):
    table = [
        (1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")
    ]
    for num, rep in table:
        if x >= num:
            return rep + solution(x-num)
    return str()


def solution9(n):
    ed = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    des = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    sot = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tys = ["", "M", "MM", "MMM", "MMMM"]

    return tys[n // 1000] + sot[n // 100 % 10] + des[n // 10 % 10] + ed[n % 10]

def solution10(n):
    ROMAN_SYMBOLS = ["M", "D", "C", "L", "X", "V", "I"]
    ROMAN_VALUES = [1000, 500, 100, 50, 10, 5, 1]
    idx = 0
    roman = []
    while n > 0:
        if n < ROMAN_VALUES[idx]:
            idx += 1
            continue
        n -= ROMAN_VALUES[idx]
        roman.append(ROMAN_SYMBOLS[idx])
        if roman[-4:].count(roman[-1]) == 4:
            roman = roman[:-3] + [ROMAN_SYMBOLS[idx-1]]
            if roman[-3:-2] == roman[-1:]:
                roman = roman[:-3] + [ROMAN_SYMBOLS[idx]] + [ROMAN_SYMBOLS[idx-2]]
    return "".join(roman)

def small(val,i,v,x):
    if val==4:
        return i + v
    if val==9:
        return i + x
    if val>5:
        return v+small(val-5,i,v,x)
    return i*val

def solution11(n):
    retVal=''
    count,n=divmod(n,1000)
    if count:
        retVal+='M'*count
    count,n=divmod(n,100)
    retVal+=small(count,'C','D','M')
    count,n=divmod(n,10)
    retVal+=small(count,'X','L','C')
    retVal+=small(n,'I','V','X')
    return retVal


def solution12(n):
    # TODO convert int to roman string
    dictionnaire = {10 ** 0: "I", 5 * 10 ** 0: "V",
                    10 ** 1: "X", 5 * 10 ** 1: "L",
                    10 ** 2: "C", 5 * 10 ** 2: "D",
                    10 ** 3: "M"}
    # I define this dictionnary to simplify comprehension and visualisation

    n = str(n)
    # I make it str because I'll use power of ten to make it easier

    n = n[::-1]
    # to use only one parameter, for power of ten and incrementations

    nb_rom = ''

    for i in range(len(n))[::-1]:
        # right to left by using powers of ten

        current = int(n[i])
        # pick up caracters one by one
        if current < 4:
            # 3 times the same sequence of caracter (III for example)
            nb_rom += current * dictionnaire[10 ** i]
            # we add the corresponding symbol

        elif current == 4:

            nb_rom += dictionnaire[10 ** i] + dictionnaire[5 * 10 ** i]

        elif current < 9:
            # works with 5,6,4,7,8
            temp = current - 5
            # we wille do V+temp*I for example so we need to know how it's higher
            nb_rom += dictionnaire[5 * 10 ** i] + temp * dictionnaire[10 ** i]

        else:
            # current==9
            nb_rom += dictionnaire[10 ** i] + dictionnaire[10 ** (i + 1)]
            # we add the current unity and the next one
            # example 9: I(10**0)X(10**1)
    return nb_rom

def solution13(n):
    numeral = ''
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10,9,5,4,1]
    numerals = ['M','CM','D','CD','C','XC','L', 'XL','X','IX','V','IV','I']
    print(numerals)
    square = lambda x, y: int(x/number[y]) * numerals[y]
    for i in range(13):
        numeral+= square(n, i)
        n = n - number[i]*int(n/number[i])
    return numeral


def solution14(data):
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))

    result = ""
    for roman, value in ROMANS:
        count = data // value
        data -= count * value
        result += roman * count

    return result

romans = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 6:'VI', 5:'V', 4:'IV', 1:'I'}
def solution15(n):
    res = ''
    for roman in romans:
        while n >= roman:
            res += romans[roman] * (n // roman)
            n %= roman
    return res

SPQR = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def solution16(n, result='', i=0):
    if i == len(SPQR):
        return result
    while n - SPQR[i][0] >= 0:
        result += SPQR[i][1]
        n -= SPQR[i][0]
    i += 1
    return solution(n, result, i)

roman = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
            (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution17(n):
    return next(r + solution(n - x) for r, x in roman if x <= n) if n > 0 else ''

SYMBOL = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}

def solution18(n):
    s = str(n)
    return ''.join(
        [solve_digit(int(char), len(s) - i - 1) for i, char in enumerate(s)]
    )

def solve_digit(digit, power_of_ten):
    base = 10**power_of_ten
    if digit == 9:
        return SYMBOL[base] + SYMBOL[base * 10]
    elif digit >= 5:
        return SYMBOL[base * 5] + SYMBOL[base] * (digit - 5)
    elif digit == 4:
        return SYMBOL[base] + SYMBOL[base * 5]
    else:
        return SYMBOL[base] * digit

def solution19(n):
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']
    return thousands[n//1000] + hundreds[n//100%10] + tens[n//10%10] + ones[n%10]

def solution20(n):
    val = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',
           10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',
          100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',
          1000:'M',0:'',2000:'MM',3000:'MMM'}
    return val[(n//1000)*1000]+val[(n%1000)-(n%100)]+val[(n%100)-(n%10)]+val[(n%10)]