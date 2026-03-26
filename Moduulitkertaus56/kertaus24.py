def kuusi(kerros):
    print("Tämä on kuusi!")
    for i in range(kerros):
        sensuri = 2 * i + 1
        valit = kerros - i - 1
        print(" " * valit + "*" * sensuri)
    valit = kerros - 1
    print(" " * valit + "*")

kerros = int(input('Kuinka ison kuusen haluat? '))
kuusi(kerros)