yazi="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

frekans=dict()

for harf in yazi:
   if harf in frekans:
       frekans[harf]+=1
   else:
       frekans[harf]=1

for i, j in frekans.items():
    print(i,":",j)