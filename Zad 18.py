def sumacyfr(liczba):
    liczba=str(liczba)
    suma=0
    for x in range(0,len(liczba)):
        suma=suma+int(liczba[x])
    print(suma)
sumacyfr(7182)