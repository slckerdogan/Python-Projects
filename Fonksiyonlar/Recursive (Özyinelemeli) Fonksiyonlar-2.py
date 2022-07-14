def toplam(liste):

    if len(liste)==1:
        return liste[0]

    else:
        return liste[0] + toplam(liste[1:])

listem=[]
sayi=int(input("Liste kaç elemanlı olsun?:"))
for i in range (1,sayi+1):
    x=int(input("Eleman:"))
    listem.append(x)
print(listem)
print(toplam(listem))