def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa
luvut = [3, 7, 13, 21, 9, 10, 69]
tulos = laske_summa(luvut)
print(f"Lista: {luvut}")
print(f"Summa: {tulos}")