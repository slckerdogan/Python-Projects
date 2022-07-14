sayi1=float(input("Lütfen birinci sayiyi giriniz:"))
sayi2=float(input("Lütfen ikinci sayiyi giriniz:"))
print("Değişmeden Önce\n1.Sayi={}\n2.Sayi={}".format(sayi1,sayi2))
sayi1,sayi2=sayi2,sayi1
print("Değiştikten Sonra\n1.Sayi={}\n2.Sayi={}".format(sayi1,sayi2))