import tkinter as tk
from tkinter import *


def topla():
    sayi1 = int(s1.get())
    sayi2 = int(s2.get())
    sonuc['text'] = sayi1 + sayi2

def ekle():
    listem.insert(tk.END, s1.get())
    s1.delete(0, tk.END)
    listem2.insert(tk.END,s2.get())
    s2.delete(0, tk.END)

def kaydet():
        f = open('Leclerc Puan.txt', 'w', encoding='utf-8')
        gorevler = listem.get(0, tk.END)
        f.writelines('\n'.join(gorevler))
        f.close()
        f2 = open('Sainz Puan.txt', 'w', encoding='utf-8')
        gorevler2 = listem2.get(0, tk.END)
        f2.writelines('\n'.join(gorevler2))
        f2.close()

def sil():
    if len(listem.curselection()) > 0:
        index = listem.curselection()[0]
        listem.delete(index)
    if len(listem2.curselection()) > 0:
        index = listem2.curselection()[0]
        listem2.delete(index)

def yukle():
    f = open('Leclerc Puan.txt', 'r', encoding='utf-8')
    gorevler = f.readlines()
    listem.delete(0, tk.END)
    for gorev in gorevler:
        if '\n' in gorev:
            gorev = gorev.replace('\n', '')
        listem.insert(tk.END, gorev)
    f2 = open('Sainz Puan.txt', 'r', encoding='utf-8')
    gorevler2 = f2.readlines()
    listem2.delete(0, tk.END)
    for gorev in gorevler2:
        if '\n' in gorev:
            gorev = gorev.replace('\n', '')
        listem2.insert(tk.END, gorev)


def pencere_olustur():
    def ekle():
        liste.insert(tk.END, giris.get())
        giris.delete(0, tk.END)

    def kaydet():
        f = open('yap.txt', 'w', encoding='utf-8')
        gorevler = liste.get(0, tk.END)
        f.writelines('\n'.join(gorevler))
        f.close()

    def sil():
        if len(liste.curselection()) > 0:
            index = liste.curselection()[0]
            liste.delete(index)

    def yukle():
        f = open('Analiz.txt', 'r', encoding='utf-8')
        gorevler = f.readlines()
        liste.delete(0, tk.END)
        for gorev in gorevler:
            if '\n' in gorev:
                gorev = gorev.replace('\n', '')
            liste.insert(tk.END, gorev)


    tl2 = Toplevel(bg="White")
    tl2.geometry("800x800")
    baslik = tk.Label(tl2, text="YARIŞ TAKVİMİ", font="Arial 22 bold", bg="white", fg="red", width=15, height=0)
    baslik.place(x=250, y=0)
    liste = Listbox(tl2, width=62, height=23, bg="White", bd=6)
    liste.place(x=210, y=90)
    giris = tk.Entry(tl2)
    giris.place(x=600, y=230)
    giris.focus()

    #giriss = tk.Entry(tl2, show="*")
    # Girdiğin şeyler yıldız olarak görünür

    #giris2 = tk.Entry(tl2, state="disabled")
    #giris2.place(x=600, y=90)
    # Giriş alanına girip birşey yazamazsın

    dugme1 = tk.Button(tl2, text="  Verileri Ekle   ",command=ekle)
    dugme1.place(x=600, y=250)
    etikettl2 = tk.Label(tl2, text="Çıkış", bg="white", fg="red", font="Arial 10 bold", height=1)
    etikettl2.place(x=650, y=450)
    buttoncikis2 = tk.Button(tl2, command=tl2.destroy, image=imaj)
    buttoncikis2.place(x=630, y=480)
    baslikyaris=tk.Label(tl2,text="Sezon Takvimi",bg="white", fg="red", font="Arial 15 bold", height=1)
    baslikyaris.place(x=30,y=40)

    baslikyaris2=tk.Label(tl2,text="Yarış Adı",bg="white", fg="red", font="Arial 10 bold", height=1)
    baslikyaris2.place(x=132,y=70)
    baslikyaris3=tk.Label(tl2,text="Tarih",bg="white", fg="red", font="Arial 10 bold", height=1)
    baslikyaris3.place(x=0,y=70)

    etiketyaris=tk.Label(tl2,text="Bahreyn\nSuudi Arabistan\nAvustralya\nE. Romagna\nMaimi\n"
                                  "İspanya\nMonaco\nAzerbaycan\nKanada\nBritanya\nAvusturya\n"
                                  "Fransa\nMacaristan\nBelçika\nHollanda\nİtalya\n"
                                  "Rusya\nSingapur\nJaponya\nAmerika\nMeksika\nBrezilya\nAbu Dhabi",
                         bg="white", fg="red", font="Arial 10 bold",state="disabled")
    etiketyaris.place(x=110,y=90)

    etiketyaris2=tk.Label(tl2,text="20.03.2022\n27.03.2022\n10.04.2022\n24.04.2022\n"
                                   "08.05.2022\n22.05.2022\n29.02.2022\n12.06.2022\n19.06.2022\n"
                                   "03.07.2022\n10.07.2022\n24.07.2022\n31.07.2022\n28.08.2022\n"
                                   "04.09.2022\n11.09.2022\n25.09.2022\n02.10.2022\n09.10.2022\n"
                                   "23.10.2022\n30.10.2022\n13.10.2022\n20.10.2022",
                         bg="white", fg="red", font="Arial 10 bold",state="disabled")
    etiketyaris2.place(x=0,y=90)

    bkaydet = tk.Button(tl2, text='Verileri kaydet', command=kaydet)
    bkaydet.place(x=600,y=280)

    bsil = tk.Button(tl2, text='    Verileri sil    ', command=sil)
    bsil.place(x=600,y=310)

    byukle = tk.Button(tl2, text='Verileri yükle  ',command=yukle)
    byukle.place(x=600,y=340)


pencere = tk.Tk()
pencere.title("FERRARİ FAN CLUB")
pencere.geometry("1000x1000")
pencere.config(bg="white")

etiket = tk.Label(pencere, text="Yarış Verileri", bg="white", fg="red", font="Arial 10 bold", height=1)
etiket.place(x=0, y=30)

resim = tk.PhotoImage(file="Ferrarilogo.png")
imaj = resim.subsample(5, 5)

button = tk.Button(image=imaj, command=pencere_olustur)
button.place(x=5, y=70)

etiket2 = tk.Label(pencere, text="Puan Tablosu", bg="white", fg="red", font="Arial 10 bold", height=1)
etiket2.place(x=450, y=30)

pilot1 = tk.Label(pencere, text="Charles Leclerc:", bg="white", fg="red", font="Arial 10 bold")
pilot1.place(x=450, y=70)

s1 = tk.Entry(width=10, bg="white", fg="black", bd=2)
s1.place(x=560, y=70)

pilot2 = tk.Label(pencere, text="Carlos Sainz:", bg="white", fg="red", font="Arial 10 bold")
pilot2.place(x=450, y=100)

s2 = tk.Entry(width=10, bg="white", fg="black", bd=2)
s2.place(x=560, y=100)

toplam = tk.Label(pencere, text="Takım Puanı:", bg="white", fg="red", font="Arial 10 bold")
toplam.place(x=450, y=125)

sonuc = tk.Label(text="- - -", font="Arial 12 bold", bg="white", width=5, fg="black")
sonuc.place(x=560, y=123)

buttontopla = tk.Button(text="Topla", bg="white", font="Verdana 10 bold", fg="purple", command=topla)
buttontopla.place(x=630, y=125)

etiket3 = tk.Label(pencere, text="Sistemden Çıkış", bg="white", fg="red", font="Arial 10 bold", height=1)
etiket3.place(x=890, y=30)

buttoncikis = tk.Button(pencere, command=pencere.destroy, image=imaj)
buttoncikis.place(x=900, y=70)


baslik=tk.Label(text="  Charles Leclerc\n  Puan Durumu",bg="white", fg="red", font="Arial 10 bold")
baslik.place(x=430,y=200)
listem = Listbox(pencere, width=3, height=23, bg="White",bd=6)
listem.place(x=480,y=250)


baslik2=tk.Label(text="    Carlos Sainz\n    Puan Durumu",bg="white", fg="red", font="Arial 10 bold")
baslik2.place(x=580,y=200)
listem2 = Listbox(pencere, width=3, height=23, bg="White",bd=6)
listem2.place(x=630,y=250)

bekle = tk.Button(pencere, text="  Puanları Ekle   ", command=ekle)
bekle.place(x=718, y=380)

bkaydet = tk.Button(pencere, text='Puanları kaydet', command=kaydet)
bkaydet.place(x=718, y=410)

bsil = tk.Button(pencere, text='    Puanları sil    ', command=sil)
bsil.place(x=718, y=440)

byukle = tk.Button(pencere, text='Puanları yükle  ', command=yukle)
byukle.place(x=718, y=470)

etiketyaris = tk.Label(pencere, text="Bahreyn→\nSuudi Arabistan→\nAvustralya→\nE. Romagna→\nMaimi→\n"
                                 "İspanya→\nMonaco→\nAzerbaycan→\nKanada→\nBritanya→\nAvusturya→\n"
                                 "Fransa→\nMacaristan→\nBelçika→\nHollanda→\nİtalya→\n"
                                 "Rusya→\nSingapur→\nJaponya→\nAmerika→\nMeksika→\nBrezilya→\nAbu Dhabi→",
                       bg="white", fg="red", font="Arial 10 bold", state="disabled")
etiketyaris.place(x=310, y=250)


pencere.mainloop()
