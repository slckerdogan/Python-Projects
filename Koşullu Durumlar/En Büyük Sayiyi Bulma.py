sayi1=float(input("Lütfen birinci sayiyi giriniz:"))
sayi2=float(input("Lütfen ikinci sayiyi giriniz:"))
sayi3=float(input("Lütfen üçüncü sayiyi giriniz:"))

if sayi1>sayi2 and sayi1>sayi3:
    print("Birinci sayi en büyüktür ve {} şeklindedir".format(sayi1))
elif sayi2>sayi1 and sayi2>sayi3:
    print("İkinci sayi en büyüktür ve {} şeklindedir".format(sayi2))
elif sayi3>sayi1 and sayi3>sayi2:
    print("Üçüncü sayi en büyüktür ve {} şeklindedir".format(sayi3))