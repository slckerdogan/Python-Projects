sayi=int(input("Lütfen bir sayi giriniz:"))
toplam=0
basamak_sayisi=len(str(sayi))
yedeksayi=sayi
while(yedeksayi>0):
   basamak_degeri=yedeksayi%10
   toplam+=basamak_degeri**basamak_sayisi
   yedeksayi=yedeksayi//10
if toplam==sayi:
    print(sayi,"Armstrong sayisidir")
else:
    print(sayi,"Armstrong sayisi değildir")