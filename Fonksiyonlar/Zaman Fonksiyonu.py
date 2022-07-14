#Kullanıcıdan saat ve dakika almalı fonksiyon oluşturun.

def zaman():
    saat=input("Lütfen saati giriniz:")
    if saat.isdigit():
        saat=int(saat)
        if ((saat>=0) and (saat<24)):
            dakika=input("Lütfen dakikayı giriniz:")
            if dakika.isdigit():
                dakika=int(dakika)
                if ((dakika >= 0) and (dakika < 60)):
                    return ("Saat= {}.{}".format(saat,dakika))
                else:
                    print("Dakika bilgisi yanlış")
            else:
                 print("Dakika veri tipi yanlış")
        else:
            print("Saat bilgisi yanlış")
    else:
        print("Saat veri tipi yanlış")

zaman=zaman()
print(zaman)