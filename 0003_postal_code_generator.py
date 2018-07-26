def generator_kodow(arg1, arg2):

    gen=[]

    dane1 = arg1[0:2]
    dane1 += arg1[3:6]
    dane1 = int(dane1)

    dane2 = arg2[0:2]
    dane2 += arg2[3:6]
    dane2 = int(dane2)

    for i in range(dane1+1, dane2, 1):
        if i%1000!= 0:
            i = str(i)
            kod = i[0:2] + '-' + i[2:5]
            gen.append(kod)
    print(gen)

string1 = '79-900'
string2 = '80-155'
generator_kodow(string1, string2)
