import tkinter as tk


def siparis_ver():
    label_siparis_bilgileri = tk.Label(form, text="Sipariş Bilgileri", bg="brown",fg="pink", font="Verdana 11 bold").place(x=10,y=350)

    ad_labeli = tk.Label(text="Ad-Soyad:", fg="pink", bg="brown", font="Verdana 11 bold").place(x=10, y=375)
    adres_labeli = tk.Label(text="Adres Bilgisi:", fg="pink", bg="brown", font="Verdana 11 bold").place(x=10, y=400)
    boyut_labeli = tk.Label(text="Boyut Bilgisi:", fg="pink", bg="brown", font="Verdana 11 bold").place(x=10, y=425)
    icindekiler_labeli = tk.Label(text="İçindekiler Bilgisi:", fg="pink", bg="brown", font="Verdana 11 bold").place(x=10, y=450)
    notlar_labeli = tk.Label(text="Notlar:", fg="pink", bg="brown", font="Verdana 11 bold").place(x=10, y=475)
    siparisteslimzamani_labeli = tk.Label(text="Sipariş Teslimi:", fg="pink", bg="brown", font="Verdana 11 bold").place(
        x=10, y=500)

    ad1_labeli = tk.Label(text=entry.get(), fg="pink", bg="brown", font="Verdana 11 bold").place(x=200, y=375)
    adres1_labeli = tk.Label(text=entry1.get(), fg="pink", bg="brown", font="Verdana 11 bold").place(x=200, y=400)
    boyut1_labeli = tk.Label(text=boyut.get(), fg="pink", bg="brown", font="Verdana 11 bold").place(x=200, y=425)
    icindekiler1_labeli = tk.Label(text=deger1.get() + " "+ deger2.get() + " " + deger3.get() + " " + deger4.get()+ " "
                  + deger5.get()+ " " + deger6.get(), fg="pink", bg="brown", font="Verdana 11 bold").place(x=200, y=450)
    notlar_labeli = tk.Label(text=entry2.get(), fg="pink", bg="brown", font="Verdana 11 bold").place(x=200, y=475)
    siparisteslimzamani_labeli=tk.Label(text=zaman.get(),fg="pink",bg="brown",font="Verdana 11 bold").place(x=200,y=500)





form=tk.Tk()
form.geometry("650x550+400+100")
form.title("Pizza Sipariş Programı")
form.config(bg="brown")

baslik=tk.Label(form,text="Pizza Sipariş Hattı",fg="pink",bg="brown",font="Verdana 18 bold").pack()


entry=tk.StringVar()
entry1=tk.StringVar()
entry2=tk.StringVar()

ad_labeli=tk.Label(text="Ad-Soyad:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=50)
adres_labeli=tk.Label(text="Adres Bilgisi:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=90)
boyut_labeli=tk.Label(text="Boyut Bilgisi:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=130)
icindekiler_labeli=tk.Label(text="İçindekiler Bilgisi:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=170)
notlar_labeli=tk.Label(text="Notlar:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=210)
siparisteslimzamani_labeli=tk.Label(text="Sipariş Teslimi:",fg="pink",bg="brown",font="Verdana 11 bold").place(x=10,y=250)

ad_entry=tk.Entry(textvariable=entry,width=74).place(x=200,y=50)
adres_entry=tk.Entry(textvariable=entry1,width=74).place(x=200,y=90)
notlar_entry=tk.Entry(textvariable=entry2,width=74,).place(x=200,y=210)


boyut=tk.StringVar()

kucukboyut_radiobutton=tk.Radiobutton(form,text="Küçük Boy",activebackground="purple",value="Küçük Boy",variable=boyut,width=14).place(x=200,y=130)
ortaboyut_radiobutton=tk.Radiobutton(form,text="Orta Boy",activebackground="purple",value="Orta Boy",variable=boyut,width=14).place(x=300,y=130)
buyukboyut_radiobutton=tk.Radiobutton(form,text="Büyük Boy",activebackground="purple",value="Büyük Boy",variable=boyut,width=14).place(x=398,y=130)
ekstrabuyukboyut_radiobutton=tk.Radiobutton(form,text="Ekstra Büyük Boy",activebackground="purple",value="Ekstra Büyük Boy",variable=boyut,width=14).place(x=523,y=130)

zaman=tk.StringVar()
hemen_radiobutton=tk.Radiobutton(form,text="Hemen",activebackground="purple",value="Hemen",variable=zaman,width=6).place(x=200,y=250)
yarimsaatsonra_radiobutton=tk.Radiobutton(form,text="30 Dakika Sonra",activebackground="purple",value="30 Dakika Sonra",variable=zaman,width=12).place(x=267,y=250)
birsaatsonra_radiobutton=tk.Radiobutton(form,text="1 Saat Sonra",activebackground="purple",value="1 Saat Sonra",variable=zaman,width=11).place(x=340,y=250)
birbucuksaatsonra_radiobutton=tk.Radiobutton(form,text="1.5 Saat Sonra",activebackground="purple",value="1.5 Saat Sonra",variable=zaman,width=12).place(x=435,y=250)
ikisaatsonra_radiobutton=tk.Radiobutton(form,text="2 Saat Sonra",activebackground="purple",value="2 Saat Sonra",variable=zaman,width=12).place(x=536,y=250)




deger1=tk.StringVar()
deger2=tk.StringVar()
deger3=tk.StringVar()
deger4=tk.StringVar()
deger5=tk.StringVar()
deger6=tk.StringVar()


icindekiler1_checkbutton=tk.Checkbutton(form,text="Sucuk",activebackground="purple",variable=deger1,onvalue="Sucuk",width=8).place(x=200,y=170)
icindekiler2_checkbutton=tk.Checkbutton(form,text="Mısır",activebackground="purple",variable=deger2,onvalue="Mısır",width=8).place(x=270,y=170)
icindekiler3_checkbutton=tk.Checkbutton(form,text="Zeytin",activebackground="purple",variable=deger3,onvalue="Zeytin",width=8).place(x=345,y=170)
icindekiler4_checkbutton=tk.Checkbutton(form,text="Biber",activebackground="purple",variable=deger4,onvalue="Biber",width=8).place(x=420,y=170)
icindekiler5_checkbutton=tk.Checkbutton(form,text="Peynir",activebackground="purple",variable=deger5,onvalue="Peynir",width=8).place(x=490,y=170)
icindekiler6_checkbutton=tk.Checkbutton(form,text="Mantar",activebackground="purple",variable=deger6,onvalue="Mantar",width=8).place(x=565,y=170)


siparis_butonu=tk.Button(form,text="Sipariş Ver",width=11,activebackground="purple",command=siparis_ver).place(x=80,y=310)


cikis_butonu=tk.Button(form,text="Çıkış",width=11,activebackground="purple",command=form.destroy).place(x=400,y=310)




form.mainloop()