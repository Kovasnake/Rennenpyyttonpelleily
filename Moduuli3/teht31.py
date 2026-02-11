omakuha = float(input("Kuinka monta senttiä kuha on?:"))
if omakuha < 37:
    huvakuha = 37 - omakuha
    print(f'Kuha on {huvakuha} cm liian pieni. Heitä se takas ja äkkiä.')
else:
    print('Pidä kalasi.')
