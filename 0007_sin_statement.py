import math as m

def main():

    #variable values
    print("Trójkat o bokach a=")
    a = int(input())
    print("i b=")
    b = int(input())
    print("oraz kącie gamma=")
    gamma_stopnie = int(input())

    #calculations
    gamma_rad = gamma_stopnie * m.pi / 180
    c = m.sqrt(a**2 + b**2 - 2*a*b*m.cos(gamma_rad))
    S = a*b* m.sin(gamma_rad)/2

    #presentation of performance
    print("\nTrójkąt o bokach a= {0}, b= {1} i kącie gamma= {2} \nma bok c={3} i powierzchnie S={4}".format(round(a,3),
    round(b,3),round(gamma_stopnie,3), round(c,3), round(S,3)))

    return 0

main()
