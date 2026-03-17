luku = int(input("Anna kokonaisluku: "))
alkuluku = True
#pitää määritellä alkuluvulle nimi
#tarkistetaan jakaja väliltä 2-luku itse
for jakaja in range(2, luku):
    if luku % jakaja != 0:
        alkuluku == True
    elif luku % jakaja == 0:
            alkuluku = False
            break # break niin on saatu tulos eikä enään lasketa
if alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")