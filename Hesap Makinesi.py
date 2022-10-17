from tkinter import *
import math


def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)

hesap = 12
s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    #print(hesap)
    #print(s1)
    giris.delete(0,'end')


s2 = 0
s3 = 0
def hesapla():
    global s2
    #print(s2)
    global hesap
    sonuc=0
    if(hesap==0):
        s2 = float(giris.get())
        sonuc = s1 + s2
    elif(hesap==1):
        s2 = float(giris.get())
        sonuc = s1 - s2
    elif (hesap == 2):
        s2 = float(giris.get())
        sonuc = s1 * s2
    elif (hesap == 3):
        s2 = float(giris.get())
        sonuc = s1 / s2
    elif (hesap==4):
        sonuc = math.cos(s1)
    elif (hesap==5):
        sonuc = math.sin(s1)
    elif (hesap==6):
        sonuc = math.tan(s1)
    elif (hesap==7):
        s2 = float(giris.get())
        sonuc = math.pow(s1,s2)
    elif (hesap==8):
        s2 = float(giris.get())
        sonuc = math.log(s1,s2)
    elif (hesap==9):
        s3 = int(s1)
        sonuc = math.factorial(s3)
    elif (hesap==10):
        s2 = float(giris.get())
        sonuc=math.pow(s1, 1 / s2)
    elif (hesap==11):
        sonuc = math.sqrt(s1)
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))


def teksil():
    metinuzunlugu = len(giris.get())
    giris.delete(metinuzunlugu-1, END)


def sifirla():
    giris.delete(0, 'end')


pencere = Tk()
pencere.geometry("350x450")
pencere.config(bg="black")
giris = Entry(font="Verdana 14 bold",bg="black",fg="white",width=23,justify=RIGHT)
giris.place(x=20,y=20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",bg="black",fg="white",command=lambda x=i:yaz(x)))

sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1

islem = []


for i in range(0,12):
    islem.append(Button(font="Verdana 14 bold",width=3,bg="black",fg="white",command=lambda x=i:islemler(x)))


islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"
islem[4]['text'] = "cos"
islem[5]['text'] = "sin"
islem[6]['text'] = "tan"
islem[7]['text'] = "us"
islem[8]['text'] = "log"
islem[9]['text'] = "fac"
islem[10]['text'] = "kök"
islem[11]['text'] = "√¯"

for i in range(0,12):
    islem[0].place(x=168, y=50)
    islem[1].place(x=168, y=100)
    islem[2].place(x=168, y=150)
    islem[3].place(x=168, y=200)
    islem[4].place(x=233, y=50)
    islem[5].place(x=233, y=100)
    islem[6].place(x=233, y=150)
    islem[7].place(x=233, y=200)
    islem[8].place(x=298, y=50)
    islem[9].place(x=298, y=100)
    islem[10].place(x=298, y=150)
    islem[11].place(x=298, y=200)




sb = Button(text="0",font="Verdana 14 bold",bg="black",fg="white",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)

nb = Button(text=".",font="Verdana 14 bold",bg="black",fg="white",width=2,command=lambda x=".":yaz(x))
nb.place(x=70,y=200)

eb = Button(text="=",fg ="RED",font="Verdana 14 bold",bg="black",command=hesapla)
eb.place(x=120,y=200)

tsb = Button(text="Sil",font="Verdana 14 bold",bg="black",fg="RED",width=12,command= teksil)
tsb.place(x=182, y=245)

cb = Button(text="C",fg ="RED",font="Verdana 14 bold",bg="black",width=12,command=sifirla)
cb.place(x=20,y=245)


pencere.mainloop()