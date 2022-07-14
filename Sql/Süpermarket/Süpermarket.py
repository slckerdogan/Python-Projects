import time
from Süpermarket_Veritabanı import *
import datetime
dir(datetime.datetime)

def menu_ekrani():
    print("""
    [1]Ürün Ekleme
    [2]Ürün Arama
    [3]Ürünleri Görüntüleme
    [4]Stok Güncelleme
    [5]Fiyat Güncelleme
    [6]Ürün Silme
    [7]Çıkış
    """)

market()

while True:
    menu_ekrani()
    giris=input("Lütfen yapmak istediğiniz işlemi seçiniz:")
    if giris=="1":
        kategori=input("Lütfen ürün kategorisini giriniz:")
        urun=input("Lütfen ürünün adını giriniz:")
        fiyat=float(input("Lütfen fiyat bilgisini giriniz:"))
        stok_durumu=int(input("Lütfen stok bilgisini giriniz:"))
        son_kullanma_tarihi=input("Lütfen son kullanma tarihini giriniz:")
        insert(kategori,urun,fiyat,stok_durumu,son_kullanma_tarihi)
        time.sleep(0.5)
        print("Kayıt işlemi başarılı")
        time.sleep(0.5)

    elif giris=="2":
        urun=input("Lütfen aramak istediğiniz ürünü giriniz:")
        if urun is not None:
            print(urun_arama(urun))

    elif giris=="3":
        time.sleep(0.5)
        urun_goruntuleme()

    elif giris=="4":
        urun_ismi=input("Lütfen stokunu güncellemek istediğiniz ürünü giriniz:")
        urun_stoku=int(input("Lütfen ürünün yeni stok miktarını giriniz:"))
        stok_guncelleme(urun_ismi,urun_stoku)
        time.sleep(0.5)
        print("Güncelleme işlemi başarılı")
        time.sleep(0.5)


    elif giris=="5":
        urun_ismi=input("Lütfen fiyatını güncellemek istediğiniz ürünü giriniz:")
        urun_fiyati=int(input("Lütfen ürünün yeni fiyatını giriniz:"))
        fiyat_guncelleme(urun_ismi,urun_fiyati)
        time.sleep(0.5)
        print("Güncelleme işlemi başarılı")
        time.sleep(0.5)

    elif giris=="6":
        tarih=input("Lütfen son kullanma tarihini yıl ay ve gün şeklinde aralarına çizgi koyarak giriniz:")
        simdi = datetime.datetime.now()
        gunun_tarihi=str(simdi.date())
        if "tarih==simdi":
            tarih2 = input("Lütfen tarihi normal giriniz:")
            urun_silme(tarih2)
            print("Ürün silme işlemi başarılı")
            time.sleep(0.5)

    elif giris=="7":
        print("Yine bekleriz")
        time.sleep(0.5)
        break

    else:
        print("Lütfen tekrar deneyiniz")
        time.sleep(0.5)