toiminto = input('Mitä haluat tehdä, kerto-, jako, yhteen- vai vähennyslasku?: ').lower()
while toiminto != 'lopeta':
    ekaluku = float(input('Anna luku: '))
    tokaluku = float(input('Anna toinen luku: '))
    if toiminto in ['kerto', 'kertolasku', 'tulo']:
        tulo = ekaluku * tokaluku
        print(f'Tulo on {tulo:.2f}')
    elif toiminto in ["jakolasku", 'jako']:
        jako = ekaluku / tokaluku
        print(f'Se on {jako:.2f}')
    elif toiminto in ["yhteenlasku", 'yhteen']:
        summa = ekaluku + tokaluku
        print(f'Se on yhteensä {summa:.2f}')
    elif toiminto in ["vähennyslasku", 'vähennys']:
        erotus = ekaluku - tokaluku
        print(f'Se on yhteensä {erotus:.2f}')
    toiminto = input('Mitä haluat tehdä, kerto-, jako, yhteen- vai vähennyslasku?: ').lower()
else:
    print('Selvä!')