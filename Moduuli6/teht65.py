def karsittu_lista(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

luvut = [3, 7, 666, 21, 9, 10, 69, 42, 5070]
karsittu = karsittu_lista(luvut)
print(f"Alkuperäinen lista: {luvut}")
print(f"Karsittu lista:     {karsittu}")