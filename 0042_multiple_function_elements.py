def count(*arg): # * słyży do określenia, że wiele argumentów może wejść do funkcji
                 # ** oznacza wiele argumentów pozycyjnych.
    return sum(arg)

print(count(2,3,4,5,10,2))
