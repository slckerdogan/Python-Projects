sayi=int(input("Lütfen bir sayi girin:"))
toplam=0

for i in range(1,sayi):
    if sayi%i==0:
        toplam+=i

if toplam==sayi:
    print("Mükemmel sayiya ulaştınız")
else:
    print("Sayi mükemmel sayi değildir")