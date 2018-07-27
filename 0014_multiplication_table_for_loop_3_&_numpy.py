#Napisz program, który wyswietli tabliczkę mnożenia

print('\n\t\tMultiplication Table\n')

for i in range(1,11) :
    for k in range(1, 11):
        print(i * k, end='\t')
    print('\n')
#Przy większej ilości danych te petle nie bd tak wydajne jak NymPy

#A teraz tablice. Napisz program, który ponumeruje pola w tablicy 4x4, od lewej do prawej \n x 4 :

import numpy as np

tab4x4 = np.linspace(1,16,16) # od 1 do 16 stwórz array 16 punktów

tab4x4 = tab4x4.reshape([4,4]) # zmień kształt na 4x4
tab4x4 = tab4x4.astype(int) #zmien typ na int

print(tab4x4)
print(tab4x4[1][3]) # sprawdzenie pozycjonowania

# Numpy pozwala używać pythona wydajniej. Generowanie pętli zajmuje za dużo czasu - czesto x 100.


#A to nie działa... wierdo :) - chodzi o sposób zapisywania danych :
nums = [1,2,3]
for x in nums :
    x = x * 10
print(nums)

# A to dziala i jest szybsze niż petle :)
nums = np.array(nums)
nums *= 10
nums - nums.astype(int)
print(nums)

# Dodaj ćwiczenie 17b 17c i 17d - potrzebujesz numpy

