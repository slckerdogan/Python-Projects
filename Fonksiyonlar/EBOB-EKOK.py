def ebob_ekok():
    x = int(input("Lütfen birinci sayiyi giriniz:"))
    y = int(input("Lütfen ikinci sayiyi giriniz:"))

    sayi1 = x
    sayi2 = y

    while y:
        x, y = y, x % y
    print("EBOB({},{})={}".format(sayi1, sayi2, x))
    print("EKOK({},{}={}".format(sayi1,sayi2,round((sayi1*sayi2)/x)))

ebob_ekok()