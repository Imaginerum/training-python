# Przećwiczenie wybranego materiału z wyrażeń słownikowych:

numbers = [1, 2, 3, 4, 5, 6]

multipliedNumbers = {
    number : number*number
    for number in numbers
}
print(multipliedNumbers)

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

fahrenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}

#Przećwiczenie materiału z wyrażeń zbioru:

names = {"arkadiusz", "Wioleta", "karol", "bartłomiej", "Jakub", "Ania"}

names = {name.capitalize() for name in names}

print(names)