import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("Montako tahkoa nopassa on?: "))
heitto = 0
while True:
    heitto += 1
    silmaluku = heita_noppaa(tahkot)
    print(f"Heitto {heitto}: {silmaluku}")
    if silmaluku == tahkot:
        print(f"{tahkot} on maksimi ja ei siihen tarvittu kuin vain {heitto}. heittoa")
        break