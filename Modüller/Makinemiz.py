import Hesap_Makinesi

while True:
    print("""
    [1] Toplama
    [2] Çıkarma
    [3] Çarpma
    [4] Bölme
    [5] Üs Alma
    [6] Kök Alma
    [7] Kosinüs Alma
    [8] Sinüs Alma
    [9] Tanjant Alma
    [10] Log Alma
    [11] Faktöriyel Alma
    [Q] Çıkış
    """)
    giris = input("Seçiminiz:")
    if giris == "1":
        print("Toplama Sonucu =", Hesap_Makinesi.topla())

    elif giris == "2":
        print("Çıkarma Sonucu =", Hesap_Makinesi.cikar())

    elif giris == "3":
        print("Çarpma Sonucu =", Hesap_Makinesi.carpim())

    elif giris == "4":
        print("Bölme Sonucu =", Hesap_Makinesi.bolme())

    elif giris == "5":
        print("Üs Sonucu =", Hesap_Makinesi.math.pow())

    elif giris == "6":
        cevap = input("Karekök mü Hesaplamak İstiyorsunuz?Cevabınız Evet ise E yoksa H harfine basın.:")
        if cevap == "E":
            print("Kök Sonucu =", Hesap_Makinesi.karekok())
        else:
            print("Kök Sonucu =", Hesap_Makinesi.kok_alma())

    elif giris == "7":
        print("Kosinüs Sonucu =", Hesap_Makinesi.cos_alma())

    elif giris == "8":
        print("Sinüs Sonucu =", Hesap_Makinesi.sin_alma())

    elif giris == "9":
        print("Tanjant Sonucu =", Hesap_Makinesi.tan_alma())

    elif giris == "10":
        print("Log Sonucu =", Hesap_Makinesi.log_alma())

    elif giris == "11":
        print("Faktöriyel Sonucu =", Hesap_Makinesi.faktoriyel_alma())

    elif giris == "q" or giris == "Q":
        print("Güle Güle")
        break
    else:
        print("Lütfen 1-11 arası seçim yapın veya çıkış yapın")
