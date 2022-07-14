with open("mailler.txt","r",encoding="utf-8") as file:
    for satir in file:
        if (satir.endswith(".com") and satir.find("@")):
            print(satir)