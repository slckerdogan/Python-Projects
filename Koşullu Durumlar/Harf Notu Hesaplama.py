vize1=float(input("Lütfen birinci vize sonucunu girin:"))
vize2=float(input("Lütfen ikinci vize sonucunu girin:"))
final=float(input("Lütfen final sonucunu girin:"))
gecme_notu=(vize1*0.3) + (vize2*0.3) + (final*0.4)

if gecme_notu>=90:
    print("AA")
elif gecme_notu>=85 and gecme_notu<90:
    print("BA")
elif gecme_notu>=80 and gecme_notu<85:
    print("BB")
elif gecme_notu>=75 and gecme_notu<80:
    print("CB")
elif gecme_notu>70 and gecme_notu<75:
    print("CC")
elif gecme_notu>=65 and gecme_notu<70:
    print("DC")
elif gecme_notu>=60 and gecme_notu<65:
    print("DD")
elif gecme_notu>=55 and gecme_notu<60:
    print("FD")
elif gecme_notu<55:
    print("FF")