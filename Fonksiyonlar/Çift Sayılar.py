from functools import reduce
def cift_mi(sayi):
    if sayi%2==0:
        return sayi

liste=[1,2,3,4,5,6,7,8,9,10]
yeni_liste=(list(filter(cift_mi,liste)))
print(yeni_liste)
print(reduce(lambda x,y:x+y,yeni_liste))


"""
2.YOL
liste=[1,2,3,4,5,6,7,8,9,10]
yeni_liste=list(filter(lambda sayi: sayi%2==0,liste))
print(yeni_liste)
print(reduce(lambda x,y:x+y,yeni_liste))
"""