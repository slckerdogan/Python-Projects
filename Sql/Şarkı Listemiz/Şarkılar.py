import time
from Şarkı_Veritabanı import *

def menu_ekrani():
    print("""
    [1]Şarkı Ekleme
    [2]Şarkı Silme
    [3]Şarkıları Görüntüleme
    [4]Prodüksiyon Şirketi Değişmişse Bunu Güncelleme
    [5]Kullanıcıdan Zaman Bilgisi Alarak Şarkı Süresini Hesaplama
    [6]Çıkış
    """)

sarki_tablosu()

while True:
    menu_ekrani()
    giris=input("Lütfen yapmak istediğiniz işlemi seçiniz:")
    if giris=="1":
        sarki_adi=input("Lütfen şarkı adını giriniz:")
        sanatci_adi=input("Lütfen sanatçı adını giriniz:")
        album_adi=input("Lütfen albüm adını giriniz:")
        produksiyon_sirket_adi=input("Lütfen prodüksiyon şirketinin adını giriniz:")
        sarki_suresi=input("Lütfen şarkı süresini giriniz:")
        insert(sarki_adi,sanatci_adi,album_adi,produksiyon_sirket_adi,sarki_suresi)
        time.sleep(0.5)
        print("Kayıt işlemi başarılı")
        time.sleep(0.5)

    elif giris=="2":
        sarki_ismi=input("Lütfen şarkı adını giriniz:")
        sarki_silme(sarki_ismi)
        print("Şarkı silme işlemi başarılı")
        time.sleep(0.5)

    elif giris=="3":
        time.sleep(0.5)
        sarkilari_yazdir()


    elif giris=="4":
        sarki_ismi=input("Lütfen şarkı adını giriniz:")
        yeni_produksiyon_sirketi=input("Lütfen yeni şirketin adını giriniz:")
        produksiyon_guncelleme(sarki_ismi,yeni_produksiyon_sirketi)
        time.sleep(0.5)
        print("Güncelleme işlemi başarılı")
        time.sleep(0.5)

    elif giris=="5":
        sure_hesapla()

    elif giris=="6":
        time.sleep(0.5)
        print("Yine bekleriz. Güle Güle")
        break

    else:
        print("Lütfen tekrar deneyiniz...")
        time.sleep(0.5)