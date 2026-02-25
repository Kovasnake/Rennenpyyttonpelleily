import random

pisteet = int(input("Montako pistettä arvotaan: "))
# laskurit
ympyras = 0
laskuri = 0
# Toistetaan kunnes päästään pisteiden määrään
while laskuri < pisteet:
    # Arvotaan pisteet
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # Katotaan onko ympyrän sisällä
    if x * x + y * y < 1:
        ympyras += 1
    laskuri += 1
piiabout = 4 * ympyras / pisteet
print(f"Piin likiarvo on: {piiabout}")