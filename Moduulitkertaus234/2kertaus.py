palkka = float(input("Mikä on tuntipalkaksi?: "))
tunnit = float(input("Montako tuntia teit töitä?: "))
paiva = input("Ja mikä päivä oli?: ").lower()
if paiva == 'sunnuntai':
    sunansio = palkka * tunnit * 2
    print(f'Päiväpalkka: {sunansio:.2f} euroa ')
else:
    peransio = palkka * tunnit
    print(f'Päiväpalkka: {peransio:.2f} euroa ')