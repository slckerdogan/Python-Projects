km_basi_ucret=float(input("Aracınızın kilometre başına ne kadar yaktığını giriniz:"))
gidilen_yol=float(input("Aracınız kaç kilometre gitti söyleyin:"))
ucret=km_basi_ucret*gidilen_yol
print("Yolculuk boyunca ödemeniz gereken ücret {} TL şeklindedir.".format(round(ucret,2)))