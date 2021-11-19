def zlicz(zdanie,litera):
    suma=0
    for x in range(0,len(zdanie)):
        if zdanie[x]==litera:
            suma+=1
    print(suma)
zlicz('You never get a second chance to make a first impression','e')