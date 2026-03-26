luvut = []
luku = input("Anna luku, nolla lopettaa: ")
while luku!="0":
    luvut.append(int(luku))
    lajiteltu = sorted(luvut)
    print(f'Lista nyt {luvut} \nLista järjestyksessä {lajiteltu} ')
    luku = input("Uusi luku: ")
print('Moro!')