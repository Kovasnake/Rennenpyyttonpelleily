satu = []
samasana = None
# toistuva sana ei ole vielä mitään eli None
while True:
    sanat = input("Anna sana lisättäväksi tarinaan: ")
    if sanat == 'loppu' or sanat == samasana:
        break
    satu.append(sanat) #sanat talteen
    samasana = sanat #kirjataan, mikä edellinen sana oli
if satu:
    print(' '.join(satu))
    # .join(muuttuja) antaa tollaisen siistin listan ja välilönti erottaa ne