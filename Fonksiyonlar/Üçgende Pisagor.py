def pisagor():
    liste = []
    for i in range(1,101):
        for j in range(1,101):
            hipotenus=((i**2) + (j**2))**0.5
            if hipotenus==int(hipotenus):
                liste.append("{},{},{}".format(i,j,int(hipotenus)))
    return liste
for i in pisagor():
    print(i)