bas_harfler=""

with open("şiir.txt","r",encoding="utf-8") as file:
    for satir in file:
        bas_harfler += satir[0]
    print(bas_harfler)