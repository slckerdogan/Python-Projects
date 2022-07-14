sekil=input("Lütfen hangi geometrik şekli hesaplamak istediğinizi söyleyiniz:")

if sekil=="Dortgen":
    kenar1=int(input("Birinci kenar:"))
    kenar2=int(input("İkinci kenar:"))
    kenar3=int(input("Üçüncü kenar:"))
    kenar4=int(input("Dördüncü kenar:"))
    if(kenar1==0 or kenar2==0 or kenar3==0 or kenar4==0):
        print("Girdiğiniz kenarlar dörtgen olma kriterlerine uymamaktadır")
    elif kenar1==kenar2 and kenar1==kenar3 and kenar1==kenar4:
        print("Bu bir karedir")
    elif kenar1==kenar2 and kenar1!=kenar3 and kenar1!=kenar4 and kenar3==kenar4:
        print("Bu bir dikdörtgendir")
    elif kenar1==kenar3 and kenar1!=kenar2 and kenar1!=kenar4 and kenar2==kenar4:
        print("Bu bir dikdörtgendir")
    elif kenar1==kenar4 and kenar1!=kenar2 and kenar1!=kenar3 and kenar2==kenar3:
        print("Bu bir dikdörtgendir")
    else:
        print("Bu bir dörtgendir")
elif sekil=="Ucgen":
    ilk_kenar = int(input("Birinci kenar:"))
    ikinci_kenar = int(input("İkinci kenar:"))
    ucuncu_kenar = int(input("Üçüncü kenar:"))
    if abs(ilk_kenar + ikinci_kenar) > ucuncu_kenar and abs(ilk_kenar + ucuncu_kenar) > ikinci_kenar and abs(ikinci_kenar + ucuncu_kenar) > ilk_kenar:
        if ilk_kenar==ikinci_kenar and ilk_kenar==ucuncu_kenar:
            print("Üçgen eşkenar üçgendir")
        elif (ilk_kenar==ikinci_kenar and ilk_kenar!=ucuncu_kenar) or (ilk_kenar==ucuncu_kenar and ilk_kenar!=ikinci_kenar) or (ikinci_kenar==ucuncu_kenar and ikinci_kenar!=ilk_kenar):
            print("Üçgen ikizkenar üçgendir")
        else:
            print("Üçgen çeşitkenar üçgendir")
    else:
        print("Girdiğiniz kenarlar üçgen olma kriterlerine uymamaktadır")
else:
    print("Lütfen doğru seçim yaptığınızdan emin olunuz")