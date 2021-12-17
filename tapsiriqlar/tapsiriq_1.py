ad = input("ad: ")
soyad = input("soyad: ")
yas = int(input("yas: "))
cins = input("cins: ")
yasadigi_s = input("y_seher: ")
maas = float(input("maas: "))
tekm = int(input("kredit: "))

print(ad, type(ad))
print(soyad, type(soyad))
print(yas, type(yas))
print(yasadigi_s, type(yasadigi_s))
print(maas, type(maas))
print(tekm+30, type(tekm))

print(ad + "/" + soyad+ "/" + str(yas))

#**********1. variant***************
if yas < 35 and yasadigi_s == "Baki" and tekm<= maas*6:
    print("uygundur")
    faiz = tekm*0.3
    ay_od = (tekm+faiz)/24
    print("ayliq odenisiniz:", ay_od)
else:
    print("uygun deyil")

#*************2. variant*************
# if yas < 35
#     print("yas uygundur")
#     if yasadigi_s == "Baki":
#         print("y seher uygundur")
#         if tekm <= maas*6 :
#             faiz = tekm*0.3
#             ay_od = (tekm+faiz)/24
#             print("ayliq odenisiniz:", ay_od)
#         else:
#             print("uygun deyil")
#     else:
#         print("y seher uygun deyil")
# else:
#     print("yas uygun deyil")

