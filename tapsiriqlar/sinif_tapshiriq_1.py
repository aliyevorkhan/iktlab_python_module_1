imtahan_1 = {}

telebe_sayisi = int(input("Zehmet olmasa telebe sayisini daxil edinL: "))

for i in range(telebe_sayisi):
    ad_soyad_bal = input("{}. telebenin melumatlarini daxil edin: ".format(i+1)).split()
    ad_soyad = ad_soyad_bal[0]+"_"+ad_soyad_bal[1] +"_"+ str(i+1)
    bal = float(ad_soyad_bal[-1])
    imtahan_1[ad_soyad] = bal
    print(imtahan_1)

cem = 0
for bal in imtahan_1.values():
    cem = cem + bal

ortalama = cem / telebe_sayisi

print("Sinifin ortalamasi: {}".format(ortalama))

for ad_soyad, bal in imtahan_1.items():
    if bal >= ortalama:
        print("Telebe {} dersi kecdi!".format(ad_soyad))
    else:
        print("Telebe {} dersden kesildi!".format(ad_soyad))
