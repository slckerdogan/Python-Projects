kilo=float(input("Lütfen kilonuzu kilogram cinsinden giriniz:"))
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz:"))
beden_kitle_endeksi=round(kilo/(boy*boy),3)

if beden_kitle_endeksi<18:
    print("Zayıfsınız...\nBeden Kitle Endeksiniz:", beden_kitle_endeksi)
elif beden_kitle_endeksi>18.5 and beden_kitle_endeksi<25:
    print("Normalsiniz...\nBeden Kitle Endeksiniz:", beden_kitle_endeksi)
elif beden_kitle_endeksi>25 and beden_kitle_endeksi<30:
    print("Fazla Kilolusunuz...\nBeden Kitle Endeksiniz:", beden_kitle_endeksi)
elif beden_kitle_endeksi>30:
    print("Obezsiniz...\nBeden Kitle Endeksiniz:", beden_kitle_endeksi)
