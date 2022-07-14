def ucgen_mi(kenar_listem):
    if abs(kenar_listem[0]+kenar_listem[1])>kenar_listem[2] and abs(kenar_listem[0]+kenar_listem[2])>kenar_listem[1] and abs(kenar_listem[1]+kenar_listem[2])>kenar_listem[0]:
        return kenar_listem



liste=[(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgen_mi,liste)))