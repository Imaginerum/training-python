"""
Znajdz liczby z zakresu 100 do 470 włącznie, które są:
- podzielne przez 7, ale niepodzielne przez 5

z czego skorzystasz?
1. generator
2. wyrażenia listowego
3. wyrażenia zbioru
4. wyrażenia słownikowego

Zastanów się czy odpowiedź na to pytanie jest zawsze taka sama?
"""
#wyrażenie listowe

numbers = [i for i in range(100, 471) if i % 7 == 0 if i % 5 != 0]

print(numbers)

#generator

numbers2 = (number for number in range(100,471) if number % 7 == 0 if number % 5 != 0)
for number in numbers2:
    print(number)