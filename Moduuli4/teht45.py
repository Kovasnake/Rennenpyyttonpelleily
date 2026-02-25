uuseri = input("Käyttäjätunnus: ")
salas = input("Salasana: ")
yritys = 1 # eli tossa oli eka yritys
while uuseri != 'python' or salas != 'rules':
    if yritys >= 5:
        print('Pääsy evätty')
        break
    print('Yritä uudelleen')
    uuseri = input("Käyttäjätunnus: ")
    salas = input("Salasana: ")
    yritys = yritys + 1
else:
    print('Tervetuloa')