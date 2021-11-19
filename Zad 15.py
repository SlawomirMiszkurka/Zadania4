import mymath
y= mymath.generate_number()
x = False

while x == False:
    if mymath.read_number() == y:
        x= True
        print("Gratulacje")