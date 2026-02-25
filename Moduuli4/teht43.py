luvut = [] # tällä saa tyhjän listan
while True:
    annaluku = input("Anna luku. Tyhjyys lopettaa: ")
    if annaluku == "":
        break
    luvut.append(float(annaluku)) # appendilla saa listattua noita numeroita talteen

if luvut:
    print(f"Pienin luku oli : {min(luvut)}")
    print(f"Suurin luku oli: {max(luvut)}") # näinkin kätevät min ja max on saatavilla
