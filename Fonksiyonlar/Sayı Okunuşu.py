birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def sayi_okuma(sayi):
    birlerbasamagi=sayi%10
    onlarbasamagi=sayi//10
    return onlar[onlarbasamagi] + " " + birler[birlerbasamagi]

sayi=int(input("Lütfen okunuşunu öğrenmek istediğiniz sayiyi giriniz:"))
print(sayi_okuma(sayi))