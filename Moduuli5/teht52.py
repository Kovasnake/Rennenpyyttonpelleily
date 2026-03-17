luvut = []
#eli nyt ei käytetä int, koska voi tulla tyhjä enter
luku = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
while luku!="":
    luvut.append(int(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")
luvut.sort(reverse=True)
print(f'Suurimmat luvut ovat {luvut[:5]}')