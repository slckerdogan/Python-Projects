import sqlite3

def market():
    conn=sqlite3.connect("Supermarket.db")
    cursor=conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS MARKET(
            kategori text,
            urun text,
            fiyat integer,
            stok integer,
            son_kullanma_tarihi text)
    """)
    conn.commit()
    conn.close()

def insert(kategori,urun,fiyat,stok,son_kullanma_tarihi):
    conn = sqlite3.connect("Supermarket.db")
    cursor = conn.cursor()
    eklenecek=""" INSERT INTO MARKET (kategori,urun,fiyat,stok,son_kullanma_tarihi) VALUES {}"""
    data=(kategori,urun,fiyat,stok,son_kullanma_tarihi)
    cursor.execute(eklenecek.format(data))
    conn.commit()
    conn.close()

def urun_arama(urun_ismi):
    conn = sqlite3.connect("Supermarket.db")
    cursor = conn.cursor()
    aranan_urun= """SELECT * from MARKET WHERE urun="{}" """
    cursor.execute(aranan_urun.format(urun_ismi))
    urun=cursor.fetchone()
    conn.close()
    return urun

def urun_goruntuleme():
    conn = sqlite3.connect("Supermarket.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * from MARKET""")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
    conn.close()

def stok_guncelleme(urun,stok):
    conn=sqlite3.connect("Supermarket.db")
    cursor=conn.cursor()
    yeni_stok = """UPDATE MARKET SET stok="{}" WHERE urun="{}"  """
    cursor.execute(yeni_stok.format(stok, urun))
    conn.commit()
    conn.close()

def fiyat_guncelleme(urun,fiyat):
    conn=sqlite3.connect("Supermarket.db")
    cursor=conn.cursor()
    yeni_stok = """UPDATE MARKET SET fiyat="{}" WHERE urun="{}"  """
    cursor.execute(yeni_stok.format(fiyat, urun))
    conn.commit()
    conn.close()

def urun_silme(tarih):
    conn=sqlite3.connect("Supermarket.db")
    cursor=conn.cursor()
    silinme = """DELETE from MARKET WHERE son_kullanma_tarihi="{}"  """
    cursor.execute(silinme.format(tarih))
    conn.commit()
    conn.close()