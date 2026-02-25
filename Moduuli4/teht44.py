import random
arpa = random.randint(1,10)
veikkaus = int(input('Sano joku kokonaisluku 1 ja 10 väliltä: '))
while veikkaus != arpa:
    if veikkaus < arpa:
        veikkaus = int(input('Sano joku suurempi: '))
    else:
        veikkaus = int(input('Sano joku pienempi: '))
print('Oikein!!!')