def gallona_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Montako gallona? (negatiivinen lopettaa): "))
    if gallonat < 0:
        print("Ei sitten")
        break
    litrat = gallona_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa")