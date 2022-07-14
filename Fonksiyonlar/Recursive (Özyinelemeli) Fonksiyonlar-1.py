def faktoriyel(n):
    if n==1 or n==0:
        return 1
    else:
        return n*faktoriyel(n-1)

sayi=int(input("Lütfen faktöriyelini istediğiniz sayiyi girin:"))
print(faktoriyel(sayi))