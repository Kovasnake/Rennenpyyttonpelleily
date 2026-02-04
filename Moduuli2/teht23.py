kanta_str=input("Mikä on suorakulmion kanta?:")
korkeus_str=input("Entä korkeus?:")
kanta=float(kanta_str)
korkeus = float(korkeus_str)
piiri=(2*kanta)+(2*korkeus)
pintala=kanta*korkeus
print('Suorakulmion pinta-ala on ' + str(pintala) + ", ja piiri on " + str(piiri))