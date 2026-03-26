snaps = ['kohta', 'eka', 'vuosi', 'on', 'ohikiitänyt', 'näkemiin']
maara = 0
for sana in snaps:
    if len(sana) >= 5:
        maara += 1
print(f'{maara} sanaa on 5 tai yli kirjainta')