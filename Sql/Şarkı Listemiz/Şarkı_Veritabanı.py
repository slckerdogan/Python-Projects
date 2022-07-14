import sqlite3

def sarki_tablosu():
    conn = sqlite3.connect("Şarkılar.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS VERITABANI(
            id integer PRIMARY KEY,
            sarki_ismi text,
            sanatci_ismi text,
            album text,
            produksiyon_sirketi text,
            sarki_suresi text)""")
    conn.commit()
    conn.close()

def insert(sarki_ismi,sanatci_ismi,album,produksiyon_sirketi,sarki_suresi):
    conn = sqlite3.connect("Şarkılar.db")
    cursor = conn.cursor()

    ekleme = """ INSERT INTO VERITABANI (sarki_ismi,sanatci_ismi,album,produksiyon_sirketi,sarki_suresi) VALUES {} """
    data = (sarki_ismi,sanatci_ismi,album,produksiyon_sirketi,sarki_suresi)
    cursor.execute(ekleme.format(data))
    conn.commit()
    conn.close()

def sarki_arama(sarki_ismi):
    conn = sqlite3.connect("Şarkılar.db.db")
    cursor = conn.cursor()

    arama = """ SELECT * from VERITABANI WHERE sarki_ismi="{}" """
    cursor.execute(arama.format(sarki_ismi))

    sarki = cursor.fetchone()
    conn.close()
    return sarki

def sarki_silme(sarki_ismi):
    conn = sqlite3.connect("Şarkılar.db")
    cursor = conn.cursor()
    silinecek_sarki=""" DELETE from VERITABANI WHERE sarki_ismi="{}" """
    cursor.execute(silinecek_sarki.format(sarki_ismi))
    conn.commit()
    conn.close()

def sarkilari_yazdir():
    conn = sqlite3.connect("Şarkılar.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT * from VERITABANI""")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
    conn.close()

def produksiyon_guncelleme(sarki_ismi, yeni_produksiyon_sirketi):
    conn = sqlite3.connect("Şarkılar.db")
    cursor = conn.cursor()

    yeni_sirket = """ UPDATE VERITABANI SET produksiyon_sirketi="{}" WHERE sarki_ismi="{}" """
    cursor.execute(yeni_sirket.format(yeni_produksiyon_sirketi, sarki_ismi))
    conn.commit()
    conn.close()

def sure_hesapla():
    saniye1 = int(input("Lütfen şarkının süresini saniye cinsinden giriniz:"))
    def dakikasaniye(san):
        if san < 60:
            print("0 dakika", san, "saniye")
        elif san >= 60:
            dak = int(san // 60)
            cevir = dak * 60
            kalansaniye = san - cevir
            print(dak, "dakika", kalansaniye, "saniye")

    def saatim(saniye):
        if saniye < 3600:
            dakikasaniye(saniye)
        elif saniye >= 3600:
            saat = int(saniye // 3600)
            saat2 = int(saat * 3600)
            kalan_saniye = int(saniye - saat2)
            print(saat, "saat", end=" ")
            dakikasaniye(kalan_saniye)

    saatim(saniye1)

