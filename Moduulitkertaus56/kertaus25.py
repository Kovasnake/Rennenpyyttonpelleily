def isoin(a, b, c):
    return max(a, b, c)
luku1 = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))
luku3 = float(input("Anna kolmas luku: "))

tulos = isoin(luku1, luku2, luku3)
print(f"Isoin kalu eiku siis luku on: {tulos}")