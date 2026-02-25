userinch = input("Sano joku tuuma, mut älä negatiivista: ")
tuumat = float(userinch)
while tuumat >= 0:
    sentit = tuumat * 2.54
    print(f'Se ois noin {sentit:.2f} senttiä oikeissa mitoissa.')
    userinch = input("Sano joku toinen tuuma, mut älä negatiivista: ")
    tuumat = float(userinch)
else:
    print('Oisit pysynyt positiivisissa luvuissa...')