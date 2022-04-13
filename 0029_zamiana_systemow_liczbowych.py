'''
ZADANIE: Zamień liczbę z jednego systemu liczbowego na kolejny
'''

print("Z jakiego systemu liczbowego będziesz zamieniał liczbę")
print("2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16")
sys_in = int(input("Podaj system wejściowy: "))
numeric_sys_in = input("Podaj liczbę: ")

numeric_sys_in_list = []
for i in numeric_sys_in:
    numeric_sys_in_list += i

nums_in_sys = {10:'A',11:'B',12:'C',13:'D',14:"E",15:'F'}

converted_num = 0
for i in range(0, len(numeric_sys_in_list)):
    if sys_in < 11:
        number = int(int(numeric_sys_in_list[i]) * sys_in ** (len(numeric_sys_in_list)-i-1))
        converted_num += number
    elif sys_in >=11:
        #converted_list = []
        #for k in nums_in_sys.keys():
        #    partial_number = k
        #    converted_list += str(partial_number)
        #    print(converted_list)
            #numeric_sys_in_list[i] = k[i]

        #print(numeric_sys_in_list)
        print("Nie potrafię konwertować z systemu",str(sys_in) + "-kowego")
        break




print()
print("Podano liczbę " + numeric_sys_in + " w " + str(sys_in) + "-tkowym systemie liczbowym.")
print("Dziesiętnie podana liczba to: " + str(converted_num))