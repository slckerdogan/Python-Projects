toplam = 0
while True:
    sayi =input("Lütfen bir sayi giriniz:")
    if (sayi=="q"):
        break
    else:
        sayi=int(sayi)
        toplam += sayi

print("Sayilarin toplamı",toplam,"şeklindedir")

