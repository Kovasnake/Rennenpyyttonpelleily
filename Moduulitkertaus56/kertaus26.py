def kertolasku(a, b):
    tulo = a * b
    print(f'Tulo on {tulo:.2f}')

def jakolasku(a, b):
    if b == 0:
        print('Virhe: Nollalla ei voi jakaa!')
    else:
        jako = a / b
        print(f'Se on {jako:.2f}')

def yhteenlasku(a, b):
    summa = a + b
    print(f'Se on yhteensä {summa:.2f}')

def vahennyslasku(a, b):
    erotus = a - b
    print(f'Se on yhteensä {erotus:.2f}')

toiminto = input('Mitä haluat tehdä, kerto-, jako, yhteen- vai vähennyslasku?: ').lower()
while toiminto != 'lopeta':
    a = float(input('Anna luku: '))
    b = float(input('Anna toinen luku: '))
    if toiminto in ['kerto', 'kertolasku', 'tulo']:
        kertolasku(a, b)
    elif toiminto in ["jakolasku", 'jako']:
        jakolasku(a,b)
    elif toiminto in ["yhteenlasku", 'yhteen']:
        yhteenlasku(a, b)
    elif toiminto in ["vähennyslasku", 'vähennys']:
        vahennyslasku(a, b)
    else:
        print('Selvä!')
    toiminto = input('Mitä haluat tehdä, kerto-, jako, yhteen- vai vähennyslasku?: ').lower()