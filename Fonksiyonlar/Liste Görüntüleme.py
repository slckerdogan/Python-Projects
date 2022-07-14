# SORU: Bir fonksiyon oluşturun. Bu fonksiyon sadece liste tipi veri alacak. Filter ve lambda ifadeleri kullanarak
# str tipi verileri filtreleyip görüntüleyeceğiz.

def str_goruntulemesi(listem):
    return[*filter(lambda x:x if type(x)==str else None,listem)]

print(str_goruntulemesi([5,6,"e"]))