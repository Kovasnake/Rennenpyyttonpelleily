nytvuosi = int(input("Mikä on vuosi nyt on?:"))
if (nytvuosi % 4 == 0 and nytvuosi % 100 != 0) or (nytvuosi % 400 == 0):
    print('Nyt on karkaus vuosi :D')
else:
    print('Nyt ei ole karkaus vuosi :(')