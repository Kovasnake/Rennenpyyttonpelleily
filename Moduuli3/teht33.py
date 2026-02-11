omasukupuoli = input("Sori mutta pitää kysyä binäärisesti. Oletko mies vai nainen?:") .lower()
hemogoblinit = float(input("Mikä on hemoglobiiniarvosi yksikössä g/l?:"))
if omasukupuoli == 'nainen':
    if hemogoblinit < 117:
        print('Tarvitset lisää rautaa, vähän matala hemoglobiini.')
    elif hemogoblinit > 175:
        print('Sulla on aika korkea määrä hemoglobiinia.')
    else:
        print('Hemoglobiinisi on normaali. Kaikki jees :D')
elif omasukupuoli == 'mies':
    if hemogoblinit < 134:
        print('Tarvitset lisää rautaa, vähän matala hemoglobiini.')
    elif hemogoblinit > 195:
        print('Sulla on aika korkea määrä hemoglobiinia.')
    else:
        print('Hemoglobiinisi on normaali. Kaikki jees :D')
else:
    print('Älä pelleile, tää on herkkää koodia.')

