class hayvan:
    def __init__(self, hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu):
        self.hayvan_adi = hayvan_adi
        self.boy = boy
        self.kilo = kilo
        self.renk = renk
        self.yasadigi_yer = yasadigi_yer
        self.beslenme_yolu = beslenme_yolu

    def bilgileri_goster(self):
        print("""
        Hayvanın Özellikleri:

        İsim :  {}
        Boy : {} metre
        Kilo: {} kilogram
        Renk :  {}
        Yaşadığı Yer: {}
        Beslenme Biçimi: {}
        """.format(self.hayvan_adi, self.boy, self.kilo, self.renk, self.yasadigi_yer, self.beslenme_yolu))


class kopek(hayvan):
    def __init__(self, species, hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu):
        super().__init__(hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu)
        self.species = species

    def bilgileri_goster1(self):
        print("""
        Köpeklerin Özellikleri:

        İsim :  {}
        Cinsi :  {}
        Boy : {} metre
        Kilo: {} kilogram
        Renk :  {}
        Yaşadığı Yer: {}
        Beslenme Biçimi: {}
        """.format(self.hayvan_adi, self.species, self.boy, self.kilo, self.renk, self.yasadigi_yer,
                   self.beslenme_yolu))


class kus(hayvan):
    def __init__(self, species, hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu):
        super().__init__(hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu)
        self.species = species

    def bilgileri_goster2(self):
        print("""
        Kuşların Özellikleri:

        İsim :  {}
        Cinsi :  {}
        Boy : {} metre
        Kilo: {} kilogram
        Renk :  {}
        Yaşadığı Yer: {}
        Beslenme Biçimi: {}
        """.format(self.hayvan_adi, self.species, self.boy, self.kilo, self.renk, self.yasadigi_yer,
                   self.beslenme_yolu))


class at(hayvan):
    def __init__(self, species, hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu):
        super().__init__(hayvan_adi, boy, kilo, renk, yasadigi_yer, beslenme_yolu)
        self.species = species

    def bilgileri_goster3(self):
        print("""
        Atların Özellikleri:

        İsim :  {}
        Cinsi :  {}
        Boy : {} metre
        Kilo: {} kilogram
        Renk :  {}
        Yaşadığı Yer: {}
        Beslenme Biçimi: {}
        """.format(self.hayvan_adi, self.species, self.boy, self.kilo, self.renk, self.yasadigi_yer,
                   self.beslenme_yolu))


print("""Hayvan Bilgisi Ekleme Sayfamıza Hoşgeldiniz
[1] Bir Hayvan Türü Ekleme
[2] Köpek Türü Ekleme
[3] Kuş Türü Ekleme
[4] At Türü Ekleme
[5] Bilgi Ekranı
    [5.1]Hayvanların Bilgileri
    [5.2]Köpeklerin Bilgileri
    [5.3]Kuşların Bilgileri
    [5.4]Atların Bilgileri
[6] Çıkış
""")
while True:
    giris = input("Yapmak istediğiniz işlemi lütfen seçiniz:")
    if giris == "1":
        adi = input("Ad:")
        boyu = float(input("Boy:"))
        kilosu = float(input("Kilosu:"))
        rengi = input("Renk:")
        yasadigi_yeri = input("Yaşadığı yer:")
        beslenme_yolu = input("Beslenme biçimi:")

        hayvanimiz = hayvan(adi, boyu, kilosu, rengi, yasadigi_yeri, beslenme_yolu)

    elif giris == "2":
        adi = input("Ad:")
        species = input("Cinsi:")
        boyu = float(input("Boy:"))
        kilosu = float(input("Kilosu:"))
        rengi = input("Renk:")
        yasadigi_yeri = input("Yaşadığı yer:")
        beslenme_yolu = input("Beslenme biçimi:")

        kopegimiz = kopek(adi, species, boyu, kilosu, rengi, yasadigi_yeri, beslenme_yolu)

    elif giris == "3":
        adi = input("Ad:")
        species = input("Cinsi:")
        boyu = float(input("Boy:"))
        kilosu = float(input("Kilosu:"))
        rengi = input("Renk:")
        yasadigi_yeri = input("Yaşadığı yer:")
        beslenme_yolu = input("Beslenme biçimi:")

        kusumuz= kus(adi, species, boyu, kilosu, rengi, yasadigi_yeri, beslenme_yolu)

    elif giris == "4":
        adi = input("Ad:")
        species = input("Cinsi:")
        boyu = float(input("Boy:"))
        kilosu = float(input("Kilosu:"))
        rengi = input("Renk:")
        yasadigi_yeri = input("Yaşadığı yer:")
        beslenme_yolu = input("Beslenme biçimi:")

        atimiz = at(adi, species, boyu, kilosu, rengi, yasadigi_yeri, beslenme_yolu)

    elif giris == "5":
        print("""Hayvan bilgi ekranı açılıyor...
        [1]Hayvanların Bilgileri
        [2]Köpeklerin Bilgileri
        [3]Kuşların Bilgileri
        [4]Atların Bilgileri
        """)
        giris = input("Yapmak istediğiniz işlemi lütfen seçiniz:")
        if giris=="1":
            hayvanimiz.bilgileri_goster()
        if giris=="2":
            kopegimiz.bilgileri_goster1()
        elif giris=="3":
            kusumuz.bilgileri_goster2()
        elif giris=="4":
            atimiz.bilgileri_goster3()

    elif giris=="6":
        print("Güle güle")
        break
    else:
        print("Doğru seçim yaptığınızdan emin olunuz")
