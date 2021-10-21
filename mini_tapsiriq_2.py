gizli_kelme = "python"
texmin = input("Kelmeni texmin ele: ")
texmin_sayisi = 1

while texmin != gizli_kelme:                                   
    print("Sizin texmin sayiniz: ", texmin_sayisi)
    texmin = input("Kelmeni tekrar texmin et: ")                       
    texmin_sayisi += 1
else:
    print("TEBRIKLER BILDIN!")                                     
