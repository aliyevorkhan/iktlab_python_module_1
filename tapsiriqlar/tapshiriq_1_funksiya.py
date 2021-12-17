def ayliq_odenis_hesabla(tekm):
    faiz = tekm*0.3
    ay_od = (tekm+faiz)/24 
    return ay_od

ad = input("ad: ")
soyad = input("soyad: ")
yas = int(input("yas: "))
cins = input("cins: ")
yasadigi_s = input("y_seher: ")
maas = float(input("maas: "))
tekm = int(input("kredit: "))

print(ad + "/" + soyad+ "/" + str(yas))

#**********1. variant***************
if yas < 35 and yasadigi_s == "Baki" and tekm<= maas*6:
    print("uygundur")
    
    ay_od = ayliq_odenis_hesabla(tekm)

    print("ayliq odenisiniz:", ay_od)
else:
    print("uygun deyil")