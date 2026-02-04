leiviska = float(input("Kuinka monta leiviskaa?:"))
naula = float(input("Kuinka monta naulaa?:"))
luoti = float(input("Kuinka monta luotia?:"))

leiviskagramma = 20*32*13.3*leiviska
naulagramma = 32*13.3*naula
luotigramma = 13.3*luoti

kaikkigrammat =luotigramma + naulagramma + leiviskagramma
kilot = kaikkigrammat//1000
grammat = kaikkigrammat%1000
print(f"Massa nykymittojen mukaan: \n{kilot:.2f} kiloa ja {grammat:.2f} grammaa.")