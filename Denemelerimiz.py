"""
sayi=int(input("Lütfen bir sayı giriniz:"))
saat=int(sayi//60)
dakika=int(sayi%60)

if saat>=24:
    orjinalsaat=saat-24
    print("Gün başından beri {} saat ve {} dakika geçti".format(orjinalsaat,dakika))
else:
    print("Gün başından beri {} saat ve {} dakika geçti".format(saat,dakika))
"""

"""
sayac=3
siralar=0
while sayac>0:
    maxmevcut=int(input("Lütfen maksimum sınıf mevcudunu girin:"))
    ögrenci=int(input("Lütfen sınıfta var olan ögrenci sayisini girin:"))
    if ögrenci>maxmevcut:
        print("Lütfen değerleri tekrar giriniz")
    else:
        if ögrenci%2==0:
            sirasayisi=int(ögrenci//2)
            siralar += sirasayisi
        else:
            sirasayisi=int(ögrenci//2)+1
            siralar+=sirasayisi
    sayac-=1
print("Alınacak sira sayisi {} tanedir".format(siralar))
"""

"""
sayi=int(input("Lütfen sayi girin:"))
toplam=((sayi//100)+(sayi//10%10)+(sayi%10))
if toplam%2==0:
    print("Basamaklar toplamı çifttir")
else:
    print("Basamaklar toplamı tektir")
print("Basamaklar toplamı:",toplam)
"""

"""
sayac=0
sayi=int(input("Lütfen sayi girin:"))
if sayi==0:
    print("{} sayisi asal değildir".format(sayi))
elif sayi==1:
    print("{} sayisi asal değildir".format(sayi))
elif sayi==2:
    print("{} sayisi asaldir".format(sayi))
else:
    for i in range(2,sayi):
        if sayi%i==0:
            sayac+=1
            if sayac>0:
                print("{} sayisi asal değildir".format(sayi))
                break
    if sayac==0:
        print("{} sayisi asaldir".format(sayi))
"""

"""
sayi=int(input("Lütfen sayi girin:"))
for i in range(1,sayi+1):
    if sayi%i==0:
        print(i, end=" ")
"""

"""
sayi=int(input("Lütfen bir sayi giriniz:"))
i=1
while i**2<=sayi:
    print(i**2,end=" ")
    i+=1
"""

"""
sayi=int(input("Lütfen bir sayi giriniz:"))
d=2
while d<=sayi:
    if sayi%d==0:
        print(d)
        sayi=sayi//d
    else:
        d=d+1
"""

"""
sayi1=int(input("Lütfen bir sayi giriniz:"))
sayi2=int(input("Lütfen bir sayi giriniz:"))
gun=1
while sayi1<=sayi2:
    sayi1=sayi1+(sayi1/100*10)
    print(sayi1)
    gun+=1
print(gun)
"""

"""
FİBONACCİ ÖRNEĞİ
a=0
b=1
sayi=int(input("Lütfen bir sayi giriniz:"))
print(a)
print(b)
while sayi>0:
    c=a+b
    print(c)
    a=b
    b=c
    sayi-=1
"""

"""
yazi=input("Lütfen bir yazı ifadesi giriniz:").split()
maksimumharflikelime=''
maksimumharflikelimeharfsayisi=0
for kelime in yazi:
    if len(kelime)>maksimumharflikelimeharfsayisi:
        maksimumharflikelime=kelime
        maksimumharflikelimeharfsayisi=len(kelime)
print(maksimumharflikelime,maksimumharflikelimeharfsayisi)
"""

"""
Palindrom Yazı Örneği

s=input("Lütfen bir ifade girin:")
t=''
for i in range(len(s)):
    if s[i]!=' ':
        t+=s[i]
print(t)
b = t[::-1]
print(b)
kontrol = True
for i in range(len(t)):
    if t[i]!=b[i]:
        kontrol= False
        break
if kontrol:
    print("Evet")
else:
    print("Hayır")
"""

"""
Şehir Oyunu

a=input("Şehir adi:")
b=input("İkinci şehir adi:")
while a[-1]==b[0]:
    a=b
    b = input("Şehir adi:")
print(b)
"""
