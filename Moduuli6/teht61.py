import random
def heita_noppaa():
    return random.randint(1, 6)
heitto = 0
while True:
    heitto += 1
    silmaluku = heita_noppaa()
    print(f"Heitto {heitto}: {silmaluku}")
    if silmaluku == 6:
        print(f"Ei mennyt kuin {heitto}. heittoa kuutoseen")
        break