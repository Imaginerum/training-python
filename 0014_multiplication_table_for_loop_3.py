#Napisz program, który wyswietli tabliczkę mnożenia

print('\n\t\tMultiplication Table\n')

for i in range(1,11) :
    for k in range(1, 11):
        print(i * k, end='\t')
    print('\n')