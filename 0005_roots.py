import math as m

#Program, który na podstawie współczynników a, b, c określi ile pierwiastków rzeczywistych ma równanie:
#ax^2 + bx + c = 0 oraz poda ich wartość.

def main():

    a = int(input('Podaj współczynniki równania ax^2 + bx + c = 0\nPodaj a= '))
    b=int(input('Podaj b= '))
    c=int(input('Podaj c= '))

    if a != 0 : #sprawdzenie czy równanie jest kwadratowe
        delta = b**2 - 4 * a * c

        if delta > 0 :
            x1 = (-b + m.sqrt(delta)) / (2 * a)
            x2 = (-b - m.sqrt(delta)) / (2* a )
            print('Równanie ma dwa pierwiastki\nx1= {0}\nx2= {1}'.format(x1,x2))

        if delta == 0 :
            x1 = (-b + m.sqrt(delta)) / (2 * a)
            print('Równanie ma jeden pierwiastek\nx1= {0}'.format(x1))

        if delta < 0 :
            print('Równanie nie ma pierwiastków rzeczywistych')

    else :
        print('Równanie ma a=0, nie jest równaniem kwadratowym')

    input()
    return 0

main()  
