def alan(kenar_listem):
    alan=kenar_listem[0] * kenar_listem[1]
    return alan

liste=[(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan,liste)))
