import math

def topla():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc = x+y
    return sonuc

def cikar():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc = x-y
    return sonuc

def carpim():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc = x*y
    return sonuc

def bolme():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc = x/y
    return sonuc

def us_alma():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc= math.pow(x,y)
    return sonuc

def karekok():
    x = float(input("Karekökü Alınacak Sayi:"))
    sonuc=math.sqrt(x)
    return sonuc

def kok_alma():
    x = float(input("Kökünü Almak İstediğiniz Sayi:"))
    y = float(input("Kaçıncı Dereceden Kökü Olsun?:"))
    if y==0:
        y = float(input("Hatalı Derece Girdiniz...Kaçıncı Dereceden Kökü Olsun?:"))
    sonuc=math.pow(x, 1/y)
    return sonuc

def cos_alma():
    x = float(input("Kosinüsünü Öğrenmek İstediğiniz Sayi:"))
    sonuc=math.cos(x)
    return sonuc

def sin_alma():
    x = float(input("Sinüsünü Öğrenmek İstediğiniz Sayi:"))
    sonuc=math.sin(x)
    return sonuc

def tan_alma():
    x = float(input("Tanjantını Öğrenmek İstediğiniz Sayi:"))
    sonuc=math.tan(x)
    return sonuc

def log_alma():
    x = float(input("Birinci Sayi:"))
    y = float(input("İkinci Sayi:"))
    sonuc=math.log(x,y)
    return sonuc

def faktoriyel_alma():
    x = int(input("Faktöriyeli Alınacak Sayi:"))
    sonuc=math.factorial(x)
    return sonuc







