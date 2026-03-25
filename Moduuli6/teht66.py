import math

def yksikkohinta(halkaisija_cm, hinta):
    sade = (halkaisija_cm / 2) / 100
    pintala = math.pi * sade ** 2
    return hinta / pintala

print("Anna Pizza 1 statsit")
halkaisija1 = float(input("Halkaisija (cm): "))
hinta1 = float(input("Hinta (€): "))

print("Anna Pizza 2 statsit")
halkaisija2 = float(input("Halkaisija (cm): "))
hinta2 = float(input("Hinta (€): "))

pizza1 = yksikkohinta(halkaisija1, hinta1)
pizza2 = yksikkohinta(halkaisija2, hinta2)
print(f"\nPizza 1: {pizza1:.2f} €/m²")
print(f"Pizza 2: {pizza2:.2f} €/m²")

if pizza1 < pizza2:
    print("Pizza 1 on kannattavampi sijoitus, paitsi jos oot cutilla.")
elif pizza2 < pizza1:
    print("Pizza 2 on kannattavampi sijoitus, paitsi jos oot cutilla.")
else:
    print("Pizzoila on sama pinta-alahinta, nauti pois.")