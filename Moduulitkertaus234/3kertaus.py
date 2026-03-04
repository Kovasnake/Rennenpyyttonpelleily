from math import sqrt
annanumero = int(input("Anna numero: "))
while annanumero != 0:
    if annanumero < 0:
        print('Virheellinen numero')
        annanumero = int(input("Anna numero: "))
    else:
        print(sqrt(annanumero))
        annanumero = int(input("Anna numero: "))
if annanumero == 0:
        print('Exiting...')