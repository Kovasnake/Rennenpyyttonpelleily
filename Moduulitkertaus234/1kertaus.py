asiakas = input("Kerro nimesi: ").lower()
if asiakas != 'matti':
    annokset =float(input("Montako keittoannosta?: "))
    summa = annokset * 5.9
    print(f'Kokonaishinta on {summa:.2f} \nSeuraava kiitos! ')
else:
    print('Seuraava kiitos!.')