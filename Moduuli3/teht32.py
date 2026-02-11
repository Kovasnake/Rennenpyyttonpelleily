omaluokka = input("Mikä on hyttiluokkanne?:").upper()
if omaluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif omaluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif omaluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif omaluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Meillä on neljä vaihtoehtoa ja et silti osannut valita oikein...')