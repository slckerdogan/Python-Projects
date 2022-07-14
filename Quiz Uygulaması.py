"""
class Soru:
    def __init__(self,soru,cevap):
        self.soru=soru
        self.cevap=cevap
sorularimiz=[
    "Cumhuriyet kaç yılında ilan edilmiştir?\na)1921\nb)1922\nc)1923",
    "Türkiye'de kaç bölge vardır?\na)6\nb)7\nc)8"
    ]

cevap_anahtari=[
    Soru(sorularimiz[0],"c"),
    Soru(sorularimiz[1],"b")
    ]


def quiz_app(cevap_anahtari):
    puan=0
    for soru in cevap_anahtari:
        cevap=input(soru.soru+"\nDoğru şıkkı işaretleyiniz:")
        if cevap==soru.cevap:
            puan+=1
    print("Sizin puanınız "+str(puan))
quiz_app(cevap_anahtari)
"""
import time


class Soru:
    def __init__(self, soru, secim, cevap):
        self.soru = soru
        self.secim = secim
        self.cevap = cevap

    def cevapkontrol(self, cevap):
        return self.cevap == cevap


class Quiz:
    def __init__(self, sorular):
        self.sorular = sorular
        self.skor = 0
        self.soruindexi = 0

    def soruyualmak(self):
        return self.sorular[self.soruindexi]

    def soruyugoster(self):
        soru = self.soruyualmak()
        print(f'Soru {self.soruindexi+1}:{soru.soru}')
        secim=input("Cevap:")
        self.tahmin(secim)
        self.soruyukle()

    def tahmin(self,secim):
        soru = self.soruyualmak()
        if soru.cevapkontrol(secim):
            time.sleep(0.5)
            print("Doğru Cevap!!!")
            self.skor+=1
            self.soruindexi+=1
            time.sleep(1)
        else:
            for q in soru.cevap:
                time.sleep(0.5)
                print("Verdiğiniz cevap yanlış olup doğru cevap " + q +" şeklindedir...")
            self.soruindexi+=1
            time.sleep(1)

    def soruyukle(self):
        if len(self.sorular) == self.soruindexi:
            self.skoryukle()
        else:
            self.ilerlemegoster()
            self.soruyugoster()
    def skoryukle(self):
        for i in range(2):
            print()
        print("Quiz sona ermiştir.Skorunuz hesaplanıyor lütfen bekleyiniz...")
        time.sleep(1.5)
        print("Toplam skorunuz: "+str(self.skor))

    def ilerlemegoster(self):
        toplamsoru=len(self.sorular)
        sorunumarasi=self.soruindexi+1

        if sorunumarasi > toplamsoru:
            print("Quiz bitti...")
        else:
            print(f"Soru {sorunumarasi} of {toplamsoru}".center(100,"*"))

q1 = Soru("Cumhuriyet kaç yılında ilan edilmiştir?\nA)1921\nB)1922\nC)1923",["A","B","C","a","b","c"],"c")
q2 = Soru("Türkiye'de kaç bölge vardır?\nA)6\nB)7\nC)8",["A","B","C","a","b","c"],"b")
q3 = Soru("Bir yıl kaç haftadır?\nA)52\nB)53\nC)51",["A","B","C","a","b","c"],"a")
sorular = [q1, q2,q3]

quiz = Quiz(sorular)
quiz.soruyukle()