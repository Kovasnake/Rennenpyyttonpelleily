import random
tulos = []
montako = int(input('Montako noppaa heitetään?: '))
for i in range(montako):
    noppa = random.randint(1, 6)
    tulos.append(noppa)
summa = sum(tulos)
print(f'Ne on yhteensä {summa}')
#kai tää toimii? toivottavasti nopat pyörii oikein