'''
2. Przećwiczenie pętli for:

Napisz program, który wygeneruje zadana liczbę wyrazów ciągu Fibonacciego.

Wzór ogólny ciągu to: nk = n(k-2) + n(k-1), każdy kolejny wyraz jest sumą dwóch poprzednich.

'''

#Ciag decymalny fibonacciego:
fib10 = int(input(print('Podal liczbe wyrazów ciagu Fibonacciego: ')))
list10 = []

for i in range(1, fib10 + 1) :
    if len(list10) >=2 and fib10!=0:
        nk = list10[i - 3] + list10[i - 2]
        list10.append(nk)
    elif len(list10) == 0 and fib10 !=0:
        list10 = [1]
    elif len(list10) == 1 and fib10 !=0:
        list10 = [1, 1]

print('Ciąg decymalny fibonacciego: {0}'.format(list10))


#ciąg binarny Fibonacciego:

list2 = []

for i in range(len(list10)):
    liczba2 = bin(list10[i])
    list2.append(liczba2)

print('\nCiąg binarny fibonacciego: {0}'.format(list2))


#ciąg octagonalny Fibonacciego:

list8 = []

for i in range(len(list10)):
    liczba8 = oct(list10[i])
    list8.append(liczba8)

print('\nCiąg oktagonalny fibonacciego: {0}'.format(list8))


#ciąg hexagonalny Fibonacciego:

list16 = []

for i in range(len(list10)):
    liczba16 = hex(list10[i])
    list16.append(liczba16)

print('\nCiąg hexagonalny fibonacciego: {0}'.format(list16))
